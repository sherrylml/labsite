from django.contrib import admin
# from labsite.bigdata.models import Members

# class MembersAdmin(admin.ModelAdmin):
# fields = ['name', 'identity']

# admin.site.register(Members, MembersAdmin)
from .models.models import *
from .models.team_models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']
admin.site.register(News, NewsAdmin)
# admin.site.register(News)

class ResDirInline(admin.StackedInline):
    model = ResDir
class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ResDirInline]
admin.site.register(Professor, ProfessorAdmin)


# for class_i in [WorkExp, ResDir, PatPri, PubInf, ResAct]:
#     admin.site.register(class_i)

for class_i in [Postgraduate]:
    admin.site.register(class_i)

