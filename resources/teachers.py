from flask import Response, request
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.models.school_teacher import SchoolTeacher
from database.models.school import School
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required


class TeachersAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar los profesores registrados",
        tags=["Teacher"],
    )
    @marshal_with(teachers_schema)
    @jwt_required()
    def get(self):
        teachers = (
            Teacher.query.filter(Teacher.status == True).order_by(Teacher.id).all()
        )
        return Response(
            teachers_schema.dumps(teachers), mimetype="application/json", status=200
        )


class TeacherAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar un profesor por su ID",
        tags=["Teacher"],
    )
    @marshal_with(teacher_schema)
    @jwt_required()
    def get(self, id):
        teacher = Teacher.query.get_or_404(id)
        return Response(
            teacher_schema.dumps(teacher), mimetype="application/json", status=200
        )

    @doc(
        description="Petición PUT para actualizar un profesor por su ID",
        tags=["Teacher"],
    )
    # @use_kwargs(teacher_schema, location=('json'))
    @marshal_with(teacher_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_teacher = Teacher.query.get_or_404(id)
        body = request.get_json()
        existing_teacher.name = body["name"]
        existing_teacher.last_name = body["last_name"]
        existing_teacher.DNI = body["DNI"]
        print(existing_teacher.id)
        if "schools" in body:
            try:
                for school_data in body["schools"]:
                    school_id = school_data["id"]
                    school = School.query.get(school_id)
                    if school and school not in existing_teacher.schools:
                        school_teacher = SchoolTeacher(
                            school_id=school.id, teacher_id=id
                        )
                        existing_teacher.schools.append(school_teacher)
            except:
                pass
        db.session.commit()
        return Response(
            teacher_schema.dumps(existing_teacher),
            mimetype="application/json",
            status=200,
        )

    @doc(
        description="Petición DELETE para eliminar un profesor por su ID",
        tags=["Teacher"],
    )
    @marshal_with(teacher_schema)
    @jwt_required()
    def delete(self, id):
        existing_teacher = Teacher.query.get_or_404(id)
        existing_teacher.status = False
        db.session.commit()
        return Response(
            teacher_schema.dumps(existing_teacher),
            mimetype="application/json",
            status=200,
        )
