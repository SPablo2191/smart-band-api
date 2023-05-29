from flask import Response, request
from flask_restful import Resource
from database.models.test import test_schema,tests_schema,test_params,Test
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

class TestsAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar las evaluaciones registradas', tags=['Test'])
    @use_kwargs(test_params, location='query')
    @marshal_with(tests_schema)
    def get(self, **kwargs):
        teacher_id = kwargs['teacher_id']
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




