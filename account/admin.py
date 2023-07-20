from django.contrib import admin
from .models import Task
from django.forms import TextInput, Textarea
from django.db import models


class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 40})},
    }


admin.site.register(Task, YourModelAdmin)