from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
docs = FlaskApiSpec()
def api_spec_conf(app):
    app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Smart Band API REST',
        version='1.0.0',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/', 
    'APISPEC_SWAGGER_UI_URL': '/'  
    })
    docs.init_app(app)