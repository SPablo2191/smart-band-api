from flask import Response, request
from flask_restful import Resource
from database.models.student import Student, student_schema, students_schema
from database.models.result import Result
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required


class StudentsAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar los estudiantes registrados",
        tags=["Student"],
    )
    @marshal_with(students_schema)
    @jwt_required()
    def get(self):
        students = (
            Student.query.filter(Student.status == True).order_by(Student.id).all()
        )
        return Response(
            students_schema.dumps(students), mimetype="application/json", status=200
        )

    @doc(description="Petición POST para añadir un nuevo estudiante", tags=["Student"])
    # @use_kwargs(student_schema, location=('json'))
    @marshal_with(student_schema)
    @jwt_required()
    def post(self, **kwargs):
        body = request.get_json()
        new_student = Student(
            name=body["name"],
            last_name=body["last_name"],
            age=body["age"],
            weight=body["weight"],
            size=body["size"],
            DNI=body["DNI"],
            seat_height=body["seat_height"],
            waist=body["waist"],
        )
        db.session.add(new_student)
        db.session.commit()
        return Response(
            student_schema.dumps(new_student), mimetype="application/json", status=200
        )


class StudentAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar un estudiante por su ID",
        tags=["Student"],
    )
    @marshal_with(student_schema)
    @jwt_required()
    def get(self, id):
        student = Student.query.get_or_404(id)
        return Response(
            student_schema.dumps(student), mimetype="application/json", status=200
        )

    @doc(
        description="Petición PUT para actualizar un estudiante por su ID",
        tags=["Student"],
    )
    # @use_kwargs(student_schema, location=('json'))
    @marshal_with(student_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_student = Student.query.get_or_404(id)
        body = request.get_json()
        result = body["result"]
        print(result)
        body.pop("result", None)
        data = Student(**body)
        existing_student.name = data.name
        new_result = Result(**result)
        existing_student.results.append(new_result)
        db.session.commit()
        return Response(
            student_schema.dumps(existing_student),
            mimetype="application/json",
            status=200,
        )

    @doc(
        description="Petición DELETE para eliminar un estudiante por su ID",
        tags=["Student"],
    )
    @marshal_with(student_schema)
    @jwt_required()
    def delete(self, id):
        existing_student = Student.query.get_or_404(id)
        existing_student.status = False
        db.session.commit()
        return Response(
            student_schema.dumps(existing_student),
            mimetype="application/json",
            status=200,
        )
