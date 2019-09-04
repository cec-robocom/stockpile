from django.contrib import admin
from components.models import user, component, history, category

admin.site.register(user)
admin.site.register(component)
admin.site.register(category)
admin.site.register(history)
