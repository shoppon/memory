import sae
from memory import wsgi
import os
import sys

root = os.path.dirname(__file__)

application = sae.create_wsgi_app(wsgi.application)

sys.path.insert(0, os.path.join(root, 'site-packages'))