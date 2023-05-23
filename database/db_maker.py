import os
from .db import db
from .models.classroom import Class
from .models.disease_student import DiseaseStudent
from .models.disease import Disease
from .models.exercise_test import ExerciseTest
from .models.exercise import Exercise
from .models.promotion_student import PromotionStudent
from .models.promotion import Promotion
from .models.result import Result
from .models.school_teacher import SchoolTeacher
from .models.school import School
from .models.status_test import StatusTest
from .models.student import Student
from .models.teacher import Teacher
from .models.test import Test


def create_db(app):
    """verificar si las tablas ya fueron creadas"""
    if not os.environ.get('TABLES_CREATED'):
        with app.app_context():
            db.create_all()
        os.environ['TABLES_CREATED'] = 'TRUE'

def drop_db(app):
    """Eliminar tablase en una base de datos """
    with app.app_context():
        db.drop_all()