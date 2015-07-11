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


'''
Team
'''
# class ResDirInline(admin.StackedInline):
class ResDirInline(admin.TabularInline):#要重启
    model = ResDir
    extra = 1
class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ResDirInline]
admin.site.register(Professor, ProfessorAdmin)

# class ResDirInline(admin.TabularInline):#要重启
#     model = ResDir
#     extra = 1
# class ProfessorAdmin(admin.ModelAdmin):
#     inlines = [ResDirInline]
# admin.site.register(Professor, ProfessorAdmin)



# for class_i in [WorkExp, ResDir, PatPri, PubInf, ResAct]:
#     admin.site.register(class_i)

for class_i in [Postgraduate]:
    admin.site.register(class_i)

