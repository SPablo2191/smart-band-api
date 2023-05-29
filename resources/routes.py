from .schools import SchoolsAPI, SchoolAPI
from .teachers import TeachersAPI, TeacherAPI
from .register import RegisterAPI
from .login import LoginAPI
from .students import StudentAPI,StudentsAPI
from .diseases import DiseaseAPI,DiseasesAPI
from .exercises import ExerciseAPI,ExercisesAPI
from .classes import ClassAPI,ClassesAPI
from .status_tests import StatusTestAPI,StatusTestsAPI
from .tests import TestsAPI
from functions.swagger import docs
url = "/api/"


def initialize_routes(api):
    api.add_resource(RegisterAPI, url + "auth/register")
    api.add_resource(LoginAPI, url + "auth/login")

    api.add_resource(TeachersAPI, url + "teachers")
    api.add_resource(TeacherAPI, url + "teachers/<int:id>")

    api.add_resource(SchoolsAPI, url + "schools")
    api.add_resource(SchoolAPI, url + "schools/<int:id>")

    api.add_resource(StudentsAPI, url + "students")
    api.add_resource(StudentAPI, url + "students/<int:id>")

    api.add_resource(DiseasesAPI, url + "diseases")
    api.add_resource(DiseaseAPI, url + "diseases/<int:id>")

    api.add_resource(ExercisesAPI, url + "exercises")
    api.add_resource(ExerciseAPI, url + "exercises/<int:id>")

    api.add_resource(ClassesAPI, url + "classes")
    api.add_resource(ClassAPI, url + "classes/<int:id>")

    api.add_resource(TestsAPI, url + "tests")
    # api.add_resource(TestAPI, url + "tests/<int:id>")

    api.add_resource(StatusTestsAPI, url + "status")
    api.add_resource(StatusTestAPI, url + "status/<int:id>")
    # add docs

def register_docs():
    docs.register(SchoolAPI)
    docs.register(SchoolsAPI)

    docs.register(TeachersAPI)
    docs.register(TeacherAPI)

    docs.register(StudentAPI)
    docs.register(StudentsAPI)

    docs.register(DiseaseAPI)
    docs.register(DiseasesAPI)

    docs.register(LoginAPI)
    docs.register(RegisterAPI)

    docs.register(ExercisesAPI)
    docs.register(ExerciseAPI)

    docs.register(ClassesAPI)
    docs.register(ClassAPI)

    docs.register(TestsAPI)
    # docs.register(TestAPI)

    docs.register(StatusTestsAPI)
    docs.register(StatusTestAPI)
