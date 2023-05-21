from .schools import SchoolsAPI,SchoolAPI
url='/api/'
def initialize_routes(api):
     api.add_resource(SchoolsAPI, url+'schools')
     api.add_resource(SchoolAPI, url+'schools/<int:id>')