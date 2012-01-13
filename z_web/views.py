# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist

from django.core import serializers
from django.utils import simplejson

import os.path
import tempfile
import string
import math
import urllib2

#from django.contrib.gis.geos import Polygon
#from django.contrib.gis.measure import Area, Distance
#from django.contrib.gis.geos import Point
#from django.contrib.gis.geos import WKBReader

from z_web.models import *

from django.core.paginator import Paginator, InvalidPage
from django.db import connections,transaction

import logging

def landing_page(request, layer=None):
    return render_to_response('landing_page.html',
                              {'pageid': 'home'},
                              context_instance=RequestContext(request))

def home_page(request, layer=None):
    return render_to_response('home.html',
                              {'pageid': 'home'},
                              context_instance=RequestContext(request))

def about_page(request, layer=None):
    return render_to_response('about.html',
                              {'pageid': 'about'},
                              context_instance=RequestContext(request))

def contact_page(request, layer=None):
    return render_to_response('contact.html',
                              {'pageid': 'contact'},
                              context_instance=RequestContext(request))

