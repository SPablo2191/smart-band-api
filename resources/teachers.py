from flask import Response, request
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db


class TeachersAPI(Resource):
    def get(self):
        teachers = Teacher.query.filter(Teacher.status == True).order_by(Teacher.id).all()
        return Response(
            teachers_schema.dumps(teachers), mimetype="application/json", status=200
        )
