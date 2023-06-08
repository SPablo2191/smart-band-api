from flask import Response, request
from flask_restful import Resource
from database.models.status_test import status_test_schema,status_tests_schema,StatusTest
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required
class StatusTestsAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar los estados de una evaluación', tags=['StatusTest'])
    @marshal_with(status_tests_schema)
    @jwt_required()
    def get(self):
        statusTests = StatusTest.query.filter(StatusTest.status == True).order_by(StatusTest.id).all()
        return Response(
            status_tests_schema.dumps(statusTests), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un estado de evaluación', tags=['StatusTest'])
    @use_kwargs(status_test_schema, location=('json'))
    @marshal_with(status_test_schema)
    @jwt_required()
    def post(self, **kwargs):
        body = request.get_json()
        new_status = StatusTest(**body)
        db.session.add(new_status)
        db.session.commit()
        return Response(
            status_test_schema.dumps(new_status), mimetype="application/json", status=200
        )


class StatusTestAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar un estado de evaluación por su ID', tags=['StatusTest'])
    @marshal_with(status_test_schema)
    @jwt_required()
    def get(self, id):
        exercise = StatusTest.query.get_or_404(id)
        return Response(
            status_test_schema.dumps(exercise), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar un estado de evaluación por su ID', tags=['StatusTest'])
    @use_kwargs(status_test_schema, location=('json'))
    @marshal_with(status_test_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_status = StatusTest.query.get_or_404(id)
        body = request.get_json()
        data = Exercise(**body)
        existing_status.name = data.name
        db.session.commit()
        return Response(
            status_test_schema.dumps(existing_status),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar un estado de evaluación por su ID', tags=['StatusTest'])
    @marshal_with(status_test_schema)
    @jwt_required()
    def delete(self, id):
        existing_status = StatusTest.query.get_or_404(id)
        existing_status.status = False
        db.session.commit()
        return Response(
            status_test_schema.dumps(existing_status),
            mimetype="application/json",
            status=200,
        )


