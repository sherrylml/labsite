from django.contrib import admin

# class MembersAdmin(admin.ModelAdmin):
# fields = ['name', 'identity']

# admin.site.register(Members, MembersAdmin)
from .models.models import *
from .models.team_models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']


for class_i in []:
    admin.site.register(class_i)
admin.site.register(News, NewsAdmin)
# admin.site.register(News)

for class_i in [Professor, Postgraduate]:
    admin.site.register(class_i)
