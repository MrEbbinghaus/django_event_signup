from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


