from flask import Response, request, make_response
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db
from functions.encrypt import bcrypt
from flask_jwt_extended import create_access_token, jwt_required


class LoginAPI(Resource):
    def post(self):
        body = request.get_json()
        email = body["email"]
        password = body["password"]
        try:
            user = Teacher.query.filter(Teacher.email == email).first()
            if not bcrypt.check_password_hash(user.password, password):
                return make_response({"error": "Contraseña incorrecta"}, 401)
            access_token = create_access_token(identity=user.DNI)
        except Exception as e:
            return make_response({"error": str(e)}, 404)
        finally:
            return Response(
                access_token, mimetype="application/json", status=200
            )
