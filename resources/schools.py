from flask import Response, request
from flask_restful import Resource
from database.models.school import school_schema, schools_schema, School
from database.db import db


class SchoolsAPI(Resource):
    def get(self):
        schools = School.query.filter(School.status == True).all()
        return Response(
            schools_schema.dumps(schools), mimetype="application/json", status=200
        )

    def post(self):
        body = request.get_json()
        new_school = School(**body)
        db.session.add(new_school)
        db.session.commit()
        return Response(
            school_schema.dumps(new_school), mimetype="application/json", status=200
        )


class SchoolAPI(Resource):
    def get(self, id):
        school = School.query.get_or_404(id)
        return Response(
            school_schema.dumps(school), mimetype="application/json", status=200
        )

    def put(self, id):
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
