from .schools import SchoolsAPI, SchoolAPI
from .teachers import TeachersAPI
from .register import RegisterAPI
from .login import LoginAPI
from .students import StudentAPI,StudentsAPI
from .diseases import DiseaseAPI,DiseasesAPI
from functions.swagger import docs
url = "/api/"


def initialize_routes(api):
    api.add_resource(RegisterAPI, url + "auth/register")
    api.add_resource(LoginAPI, url + "auth/login")
    api.add_resource(TeachersAPI, url + "teachers")
    api.add_resource(SchoolsAPI, url + "schools")
    api.add_resource(SchoolAPI, url + "schools/<int:id>")
    api.add_resource(StudentsAPI, url + "students")
    api.add_resource(StudentAPI, url + "students/<int:id>")
    api.add_resource(DiseasesAPI, url + "diseases")
    api.add_resource(DiseaseAPI, url + "diseases/<int:id>")
    # add docs

def register_docs():
    docs.register(SchoolAPI)
    docs.register(SchoolsAPI)
    docs.register(TeachersAPI)
    docs.register(StudentAPI)
    docs.register(StudentsAPI)
    docs.register(DiseaseAPI)
    docs.register(DiseasesAPI)
    docs.register(LoginAPI)
    docs.register(RegisterAPI)
