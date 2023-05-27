from flask import Response, request
from flask_restful import Resource
from database.models.school import school_schema, schools_schema, School
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

class SchoolsAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar los colegios', tags=['School'])
    @marshal_with(schools_schema)
    def get(self):
        schools = School.query.filter(School.status == True).order_by(School.id).all()
        return Response(
            schools_schema.dumps(schools), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un nuevo colegio', tags=['School'])
    @use_kwargs(school_schema, location=('json'))
    @marshal_with(school_schema)
    def post(self, **kwargs):
        body = request.get_json()
        new_school = School(**body)
        db.session.add(new_school)
        db.session.commit()
        return Response(
            school_schema.dumps(new_school), mimetype="application/json", status=200
        )


class SchoolAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar un colegio por su ID', tags=['School'])
    @marshal_with(school_schema)
    def get(self, id):
        school = School.query.get_or_404(id)
        return Response(
            school_schema.dumps(school), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar un colegio por su ID', tags=['School'])
    @use_kwargs(school_schema, location=('json'))
    @marshal_with(school_schema)
    def put(self, id, **kwargs):
        existing_school = School.query.get_or_404(id)
        body = request.get_json()
        data = School(**body)
        existing_school.name = data.name
        db.session.commit()
        return Response(
            school_schema.dumps(existing_school),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar un colegio por su ID', tags=['School'])
    @marshal_with(school_schema)
    def delete(self, id):
        existing_school = School.query.get_or_404(id)
        existing_school.status = False
        db.session.commit()
        return Response(
            school_schema.dumps(existing_school),
            mimetype="application/json",
            status=200,
        )


