from django.contrib import admin
from ticketing.models import Ticketing,Cinemas
# Register your models here.
admin.site.register([Ticketing,Cinemas])