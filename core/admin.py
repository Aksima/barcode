import inspect
from . import models
from django.contrib import admin

for _, model in inspect.getmembers(models, inspect.isclass):
    admin.site.register(model)
