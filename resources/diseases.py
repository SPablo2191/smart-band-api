from flask import Response, request
from flask_restful import Resource
from database.models.disease import Disease,disease_schema,diseases_schema
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required
class DiseasesAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar las enfermedades', tags=['Disease'])
    @marshal_with(diseases_schema)
    @jwt_required()
    def get(self):
        diseases = Disease.query.filter(Disease.status == True).order_by(Disease.id).all()
        return Response(
            diseases_schema.dumps(diseases), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un nueva enfermedad', tags=['Disease'])
    @use_kwargs(disease_schema)
    @marshal_with(disease_schema)
    @jwt_required()
    def post(self, **kwargs):
        body = request.get_json()
        new_disease = Disease(**body)
        db.session.add(new_disease)
        db.session.commit()
        return Response(
            disease_schema.dumps(new_disease), mimetype="application/json", status=200
        )


class DiseaseAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar una enfermedad por su ID', tags=['Disease'])
    @marshal_with(disease_schema)
    @jwt_required()
    def get(self, id):
        disease = Disease.query.get_or_404(id)
        return Response(
            disease_schema.dumps(disease), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar una enfermedad por su ID', tags=['Disease'])
    @use_kwargs(disease_schema, location=('json'))
    @marshal_with(disease_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_disease = Disease.query.get_or_404(id)
        body = request.get_json()
        data = Disease(**body)
        existing_disease.name = data.name
        db.session.commit()
        return Response(
            disease_schema.dumps(existing_disease),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar una enfermedad por su ID', tags=['Disease'])
    @marshal_with(disease_schema)
    @jwt_required()
    def delete(self, id):
        existing_disease = Disease.query.get_or_404(id)
        existing_disease.status = False
        db.session.commit()
        return Response(
            disease_schema.dumps(existing_disease),
            mimetype="application/json",
            status=200,
        )


