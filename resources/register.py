from flask import Response, request,make_response
from flask_restful import Resource
from database.models.teacher import Teacher, teacher_schema
from database.models.school_teacher import SchoolTeacher
from database.db import db
from functions.encrypt import bcrypt

class RegisterAPI(Resource):
    def post(self):
        body = request.get_json()
        schools = body['schools']
        body.pop('schools',None)
        new_teacher = Teacher(**body)
        new_teacher.password = bcrypt.generate_password_hash(new_teacher.password)
        teacher_schools = []
        db.session.add(new_teacher)
        try: 
            db.session.commit()
            for school in schools:
                new_teacher_school = SchoolTeacher(school_id=school['id'],teacher_id=new_teacher.id)
                teacher_schools.append(new_teacher_school)
            db.session.add_all(teacher_schools)
            db.session.commit()
        except:
            return make_response({"error": "No se pudo registrar al usuario"}, 400)
        return Response(
            teacher_schema.dumps(new_teacher), mimetype="application/json", status=200
        )
