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

admin.site.register(Notices, NewsAdmin)
admin.site.register(Academic, NewsAdmin)
admin.site.register(Meetings, NewsAdmin)
admin.site.register(Relax, NewsAdmin)
admin.site.register(Join1, NewsAdmin)
admin.site.register(Join2, NewsAdmin)
admin.site.register(Lab)

'''
Team
'''

class ResDirInline(admin.TabularInline):  # 要重启runserver
    model = ResDir
    extra = 1


class WorkExpInline(admin.TabularInline):
    model = WorkExp
    extra = 1


class PatPriInline(admin.TabularInline):
    model = PatPri
    extra = 1


class PubInfInline(admin.TabularInline):
    model = PubInf
    extra = 1


class ResActInline(admin.TabularInline):
    model = ResAct
    extra = 1


class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ResDirInline, WorkExpInline, PatPriInline, PubInfInline, ResActInline]


admin.site.register(Professor, ProfessorAdmin)


class ResDirInline1(admin.TabularInline):  # 要重启runserver
    model = ResDir1
    extra = 1


class WorkExpInline1(admin.TabularInline):
    model = WorkExp1
    extra = 1


class PatPriInline1(admin.TabularInline):
    model = PatPri1
    extra = 1


class PubInfInline1(admin.TabularInline):
    model = PubInf1
    extra = 1


class ResActInline1(admin.TabularInline):
    model = ResAct1
    extra = 1


class PostgraduateAdmin(admin.ModelAdmin):
    inlines = [ResDirInline1, WorkExpInline1, PatPriInline1, PubInfInline1, ResActInline1]


admin.site.register(Postgraduate, PostgraduateAdmin)

# for class_i in [WorkExp, ResDir, PatPri, PubInf, ResAct]:
# admin.site.register(class_i)

