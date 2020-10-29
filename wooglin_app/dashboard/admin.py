from django.contrib import admin
from dashboard.models import Members
from dashboard.models import SoberBros
from dashboard.models import SoberBroSheets

# Register your models here.
admin.site.register(Members)
admin.site.register(SoberBros)
admin.site.register(SoberBroSheets)


