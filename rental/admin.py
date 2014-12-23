# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    search_fields = ['who', 'what']
    ordering = ['who']
  
    
      
  
admin.site.register(Rental, RentalAdmin)