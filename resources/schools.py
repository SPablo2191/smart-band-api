from flask import Response, request
from flask_restful import Resource
from database.models.school import school_schema, schools_schema, School


class SchoolsAPI(Resource):
    def get(self):
        schools = School.query.filter(School.status == True).all()
        return Response(
            schools_schema.dumps(schools), mimetype="application/json", status=200
        )


class SchoolAPI(Resource):
    def get(self, id):
        school = School.query.get_or_404(id)
        return Response(
            school_schema.dump(school), mimetype="application/json", status=200
        )
    
