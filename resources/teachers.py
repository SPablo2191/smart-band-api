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



class TeacherAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar un profesor por su ID', tags=['Teacher'])
    @marshal_with(teacher_schema)
    def get(self, id):
        teacher = Teacher.query.get_or_404(id)
        return Response(
            teacher_schema.dumps(teacher), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar un profesor por su ID', tags=['Teacher'])
    @use_kwargs(teacher_schema, location=('json'))
    @marshal_with(teacher_schema)
    def put(self, id, **kwargs):
        existing_teacher = Teacher.query.get_or_404(id)
        body = request.get_json()
        data = Teacher(**body)
        existing_teacher.name = data.name
        db.session.commit()
        return Response(
            teacher_schema.dumps(existing_teacher),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar un profesor por su ID', tags=['Teacher'])
    @marshal_with(teacher_schema)
    def delete(self, id):
        existing_teacher = Teacher.query.get_or_404(id)
        existing_teacher.status = False
        db.session.commit()
        return Response(
            teacher_schema.dumps(existing_teacher),
            mimetype="application/json",
            status=200,
        )
