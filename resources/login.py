from flask import Response, request,make_response
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db
from functions.encrypt import bcrypt

class LoginAPI(Resource):
    def post(self):
        body = request.get_json()
        email = body['email']
        password = body['password']
        try:
            user = Teacher.query.filter(Teacher.email==email).first()
            print(user.password,password)
            if(bcrypt.check_password_hash(user.password, password)):
                print("Inicio de sesion exitoso")
        except Exception as e:
            return make_response({"error": str(e)}, 404)
