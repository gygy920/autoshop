from django.contrib import admin
from .models import Mark
from .models import Color
from .models import Type
from .models import Car
# Register your models here.
admin.site.register(Mark)
admin.site.register(Color)
admin.site.register(Type)
admin.site.register(Car)
