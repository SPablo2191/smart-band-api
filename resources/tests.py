from flask import Response, request
from flask_restful import Resource
from database.models.test import test_schema,tests_schema,test_params,Test
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required

class TestsAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar las evaluaciones registradas de un profesor', tags=['Test'])
    @marshal_with(tests_schema)
    @jwt_required()
    def get(self, teacher_id):
        tests = Test.query.filter(Test.status == True,Test.teacher_id==teacher_id).order_by(Test.id).all()
        return Response(
            tests_schema.dumps(tests), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un nueva evaluación', tags=['Test'])
    @use_kwargs(test_schema)
    @marshal_with(test_schema)
    def post(self, **kwargs):
        body = kwargs
        new_test = Test(**body)
        db.session.add(new_test)
        db.session.commit()
        return Response(
            test_schema.dumps(new_test), mimetype="application/json", status=200
        )



class TestAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar una evaluación por el id del profesor y de la promoción', tags=['Test'])
    @marshal_with(test_schema)
    def get(self, teacher_id,promotion_id):
        test = Test.query.filter_by(teacher_id=teacher_id,promotion_id=promotion_id).first()
        return Response(
            test_schema.dumps(test), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar una evaluación por el id del profesor y de la promoción', tags=['Test'])
    @use_kwargs(test_schema, location=('json'))
    @marshal_with(test_schema)
    def put(self, teacher_id,promotion_id, **kwargs):
        existing_test = Test.query.filter_by(teacher_id=teacher_id,promotion_id=promotion_id).first()
        body = kwargs
        data = test_schema(**body)
        existing_test.name = data.name
        db.session.commit()
        return Response(
            test_schema.dumps(existing_test),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar una evaluación por el id del profesor y de la promoción', tags=['Test'])
    @marshal_with(test_schema)
    def delete(self, teacher_id,promotion_id):
        existing_test = Test.query.filter_by(teacher_id=teacher_id,promotion_id=promotion_id).first()
        existing_test.status = False
        db.session.commit()
        return Response(
            test_schema.dumps(existing_test),
            mimetype="application/json",
            status=200,
        )




