from flask import Response, request
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

class TeachersAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar los profesores registrados', tags=['Teacher'])
    @marshal_with(teachers_schema)
    def get(self):
        teachers = Teacher.query.filter(Teacher.status == True).order_by(Teacher.id).all()
        return Response(
            teachers_schema.dumps(teachers), mimetype="application/json", status=200
        )
