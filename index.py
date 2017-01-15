from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
import os

@view_config(route_name='hello', renderer='string')
def hello_world(request):
    return 'Hello World'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8080'))
    config = Configurator()
    config.add_route('hello', '/')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
