from .schools import SchoolsAPI, SchoolAPI
from .teachers import TeachersAPI
from .register import RegisterAPI
from .login import LoginAPI

url = "/api/"


def initialize_routes(api):
    api.add_resource(SchoolsAPI, url + "schools")
    api.add_resource(SchoolAPI, url + "schools/<int:id>")
    api.add_resource(TeachersAPI, url + "teachers")
    api.add_resource(RegisterAPI, url + "register")
    api.add_resource(LoginAPI, url + "register")
