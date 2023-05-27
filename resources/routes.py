from .schools import SchoolsAPI, SchoolAPI
from .teachers import TeachersAPI
from .register import RegisterAPI
from .login import LoginAPI
from .students import StudentAPI,StudentsAPI
from functions.swagger import docs
url = "/api/"


def initialize_routes(api):
    api.add_resource(RegisterAPI, url + "authentication/register")
    api.add_resource(LoginAPI, url + "authentication/login")
    api.add_resource(TeachersAPI, url + "teachers")
    api.add_resource(SchoolsAPI, url + "schools")
    api.add_resource(SchoolAPI, url + "schools/<int:id>")
    api.add_resource(StudentsAPI, url + "students")
    api.add_resource(StudentAPI, url + "students/<int:id>")
    # add docs
    docs.register(SchoolAPI)
    docs.register(SchoolsAPI)
    docs.register(TeachersAPI)
    docs.register(StudentAPI)
    docs.register(StudentsAPI)
    docs.register(LoginAPI)
    docs.register(RegisterAPI)

