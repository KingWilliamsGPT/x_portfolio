from django.contrib import admin

from  . import models


admin.site.register(models.UserProfile)
admin.site.register(models.Skill)
admin.site.register(models.Title)
admin.site.register(models.Project)
admin.site.register(models.Category)
