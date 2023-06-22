from flask import Response, request
from flask_restful import Resource
from database.models.promotion import promotion_schema, promotions_schema, Promotion
from database.models.student import Student
from database.models.promotion_student import PromotionStudent
from database.db import db
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_jwt_extended import jwt_required


class PromotionsAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar las promociones de un colegio",
        tags=["Promotion"],
    )
    @marshal_with(promotions_schema)
    @jwt_required()
    def get(self, school_id):
        promotions = (
            Promotion.query.filter(
                Promotion.status == True, Promotion.school_id == school_id
            )
            .order_by(Promotion.id)
            .all()
        )
        return Response(
            promotions_schema.dumps(promotions), mimetype="application/json", status=200
        )

    @doc(
        description="Petición POST para añadir una nueva promocion", tags=["Promotion"]
    )
    # @use_kwargs(promotion_schema, location=('json'))
    @marshal_with(promotion_schema)
    @jwt_required()
    def post(self, school_id, **kwargs):
        body = request.get_json()
        students = body.pop("students", [])
        new_promotion = Promotion(**body)
        db.session.add(new_promotion)
        db.session.commit()
        for student_data in students:
            student = Student(**student_data)
            promotion_student = PromotionStudent(
                promotion_id=new_promotion.id, student_id=student.id
            )
            db.session.add(promotion_student)

        db.session.commit()
        return Response(
            promotion_schema.dumps(new_promotion),
            mimetype="application/json",
            status=200,
        )


class PromotionAPI(MethodResource, Resource):
    @doc(
        description="Petición GET para recuperar una promoción por su ID",
        tags=["Promotion"],
    )
    @marshal_with(promotion_schema)
    @jwt_required()
    def get(self, id):
        promotion = Promotion.query.get_or_404(id)
        return Response(
            promotion_schema.dumps(promotion), mimetype="application/json", status=200
        )

    @doc(
        description="Petición PUT para actualizar una promoción por su ID",
        tags=["Promotion"],
    )
    # @use_kwargs(promotion_schema, location=('json'))
    @marshal_with(promotion_schema)
    @jwt_required()
    def put(self, id, **kwargs):
        existing_promotion = Promotion.query.get_or_404(id)
        body = request.get_json()
        data = Promotion(**body)
        existing_promotion.name = data.name
        db.session.commit()
        return Response(
            promotion_schema.dumps(existing_promotion),
            mimetype="application/json",
            status=200,
        )

    @doc(
        description="Petición DELETE para eliminar una promoción por su ID",
        tags=["Promotion"],
    )
    @marshal_with(promotion_schema)
    @jwt_required()
    def delete(self, id):
        existing_promotion = Promotion.query.get_or_404(id)
        existing_promotion.status = False
        db.session.commit()
        return Response(
            promotion_schema.dumps(existing_promotion),
            mimetype="application/json",
            status=200,
        )
