from django.contrib import admin
from components.models import user, component, history

admin.site.register(user)
admin.site.register(component)
admin.site.register(history)
