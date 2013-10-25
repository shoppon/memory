from django.utils.importlib import import_module

def import_dotted_path(path):
    try:
        module_path, member_name = path.rsplit(".", 1)
        module = import_module(module_path)
        return getattr(module, member_name)
    except (ValueError, ImportError, AttributeError), e:
        raise ImportError("Could not import the name: %s: %s" % (path, e))