from flask import Response, request
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db
from functions.encrypt import bcrypt

class RegisterAPI(Resource):
    def post(self):
        body = request.get_json()
        new_teacher = Teacher(**body)
        new_teacher.password = bcrypt.generate_password_hash(new_teacher.password)
        print(new_teacher.password)
        # db.session.add(new_teacher)
        # db.session.commit()
        return Response(
            teacher_schema.dumps(new_teacher), mimetype="application/json", status=200
        )
