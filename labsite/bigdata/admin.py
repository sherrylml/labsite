from django.contrib import admin
from .models.models import *
from .models.team_models import *
# from nested_inlines.admin import NestedModelAdmin


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']


admin.site.register(News, NewsAdmin)
# admin.site.register(News)

for i in [Notices, Academic, Meetings, Relax, Join1, Join2, ]:
    admin.site.register(i, NewsAdmin)


class inlineBase(admin.TabularInline):
    extra = 1


'''
教授相关信息
'''


class ResDirInline(inlineBase):  # 要重启runserver
    model = ResDir


class WorkExpInline(inlineBase):
    model = WorkExp


class PatPriInline(inlineBase):
    model = PatPri


class PubInfInline(inlineBase):
    model = PubInf


class ResActInline(inlineBase):
    model = ResAct


class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ResDirInline, WorkExpInline, PatPriInline, PubInfInline, ResActInline]


admin.site.register(Professor, ProfessorAdmin)

'''
学生相关信息
'''


class ResDirInline1(inlineBase):  # 要重启runserver
    model = ResDir1


class WorkExpInline1(inlineBase):
    model = WorkExp1


class PatPriInline1(inlineBase):
    model = PatPri1


class PubInfInline1(inlineBase):
    model = PubInf1


class ResActInline1(inlineBase):
    model = ResAct1


class PostgraduateAdmin(admin.ModelAdmin):
    inlines = [ResDirInline1, WorkExpInline1, PatPriInline1, PubInfInline1, ResActInline1]


admin.site.register(Postgraduate, PostgraduateAdmin)

'''
实验室相关信息
'''


# class ImagesInline(inlineBase):
#     model = Images


class DirectionsInline(inlineBase):
    model = Directions
    # inlines = [ImagesInline, ]


class LabAdmin(admin.ModelAdmin):
    inlines = [DirectionsInline]


admin.site.register(Lab, LabAdmin)

# for class_i in [WorkExp, ResDir, PatPri, PubInf, ResAct]:
# admin.site.register(class_i)

