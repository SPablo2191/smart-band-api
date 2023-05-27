from flask import Response, request
from flask_restful import Resource
from database.models.exercise import exercise_schema,exercises_schema,Exercise
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

class ExercisesAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar los ejercicios', tags=['Exercise'])
    @marshal_with(exercises_schema)
    def get(self):
        exercises = Exercise.query.filter(Exercise.status == True).order_by(Exercise.id).all()
        return Response(
            exercises_schema.dumps(exercises), mimetype="application/json", status=200
        )
    @doc(description='Petición POST para añadir un nuevo ejercicio', tags=['Exercise'])
    @use_kwargs(exercise_schema, location=('json'))
    @marshal_with(exercise_schema)
    def post(self, **kwargs):
        body = request.get_json()
        new_exercise = Exercise(**body)
        db.session.add(new_exercise)
        db.session.commit()
        return Response(
            exercise_schema.dumps(new_exercise), mimetype="application/json", status=200
        )


class ExerciseAPI(MethodResource,Resource):
    @doc(description='Petición GET para recuperar un ejercicio por su ID', tags=['Exercise'])
    @marshal_with(exercise_schema)
    def get(self, id):
        exercise = Exercise.query.get_or_404(id)
        return Response(
            exercise_schema.dumps(exercise), mimetype="application/json", status=200
        )

    @doc(description='Petición PUT para actualizar un ejercicio por su ID', tags=['Exercise'])
    @use_kwargs(exercise_schema, location=('json'))
    @marshal_with(exercise_schema)
    def put(self, id, **kwargs):
        existing_exercise = Exercise.query.get_or_404(id)
        body = request.get_json()
        data = Exercise(**body)
        existing_exercise.name = data.name
        db.session.commit()
        return Response(
            exercise_schema.dumps(existing_exercise),
            mimetype="application/json",
            status=200,
        )
    @doc(description='Petición DELETE para eliminar un colegio por su ID', tags=['Exercise'])
    @marshal_with(exercise_schema)
    def delete(self, id):
        existing_exercise = Exercise.query.get_or_404(id)
        existing_exercise.status = False
        db.session.commit()
        return Response(
            exercise_schema.dumps(existing_exercise),
            mimetype="application/json",
            status=200,
        )


