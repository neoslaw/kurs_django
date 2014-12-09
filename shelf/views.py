# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Author

class AuthorListView(ListView):
    model = Author
    
class AuthorDetailView(DetailView):
    model = Author
    
    