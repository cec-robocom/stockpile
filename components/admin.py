from django.contrib import admin
from components.models import User, Component, History, Category

admin.site.register(User)
admin.site.register(Component)
admin.site.register(Category)
admin.site.register(History)
