from flask import Response, request
from flask_restful import Resource
from database.models.classroom import classes_schema,class_schema,Class
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required
class ClassesAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar los cursos', tags=['Class'])
    @marshal_with(classes_schema)
    @jwt_required()
    def get(self):
        classes = Class.query.filter(Class.status == True).order_by(Class.id).all()
        return Response(
            classes_schema.dumps(classes), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un nuevo curso', tags=['Class'])
    # @use_kwargs(class_schema, location=('json'))
    # @marshal_with(class_schema)
    @jwt_required()
    def post(self, **kwargs):
        body = request.get_json()
        new_class = Class(**body)
        db.session.add(new_class)
        db.session.commit()
        return Response(
            class_schema.dumps(new_class), mimetype="application/json", status=200
        )


class ClassAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar un curso por su ID', tags=['Class'])
    @marshal_with(class_schema)
    @jwt_required()
    def get(self, id):
        classroom = Class.query.get_or_404(id)
        return Response(
            class_schema.dumps(classroom), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar un curso por su ID', tags=['Class'])
    # @use_kwargs(class_schema, location=('json'))
    @marshal_with(class_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_class = Class.query.get_or_404(id)
        body = request.get_json()
        data = Class(**body)
        existing_class.name = data.name
        db.session.commit()
        return Response(
            class_schema.dumps(existing_class),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para curso un colegio por su ID', tags=['Class'])
    @marshal_with(class_schema)
    @jwt_required()
    def delete(self, id):
        existing_class = Class.query.get_or_404(id)
        existing_class.status = False
        db.session.commit()
        return Response(
            class_schema.dumps(existing_class),
            mimetype="application/json",
            status=200,
        )


