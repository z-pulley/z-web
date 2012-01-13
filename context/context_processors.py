from django.conf import settings

def root_url(request):
    """
    """
    return {'root_url':settings.ROOT_URL}

def root_relative_url(request):
    """
    """
    return {'root_relative_url':settings.ROOT_RELATIVE_URL}

def databases(request):
    """
    """
    return {'databases':settings.DATABASES}

