from flask import Response, request
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema, teachers_schema
from database.db import db
from functions.encrypt import bcrypt

class LoginAPI(Resource):
    def post(self):
        pass
