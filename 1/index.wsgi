import sae
from memory import wsgi

application = sae.create_wsgi_app(wsgi.application)