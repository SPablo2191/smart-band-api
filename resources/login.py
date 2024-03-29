from flask import Response, request, make_response
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, login_schema
from database.db import db
from functions.encrypt import bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import datetime

class LoginAPI(MethodResource,Resource):
    @doc(description='Petición POST para iniciar sesión', tags=['Authentication'])
    @use_kwargs(login_schema, location=('json'))
    @marshal_with(teacher_schema)
    def post(self, **kwargs):
        body = request.get_json()
        email = body["email"]
        password = body["password"]
        try:
            user = Teacher.query.filter(Teacher.email == email).first()
            if not bcrypt.check_password_hash(user.password, password):
                return make_response({"error": "Contraseña incorrecta"}, 401)
            expires = datetime.timedelta(minutes=30)
            access_token = create_access_token(identity=user.DNI)
            return make_response({'access_token': access_token, 'user_id': user.id},200)
        except Exception as e:
            return make_response({"error": str(e)}, 404)
