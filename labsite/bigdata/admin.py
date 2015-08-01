from django.contrib import admin
from .models.models import *
from .models.team_models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']


admin.site.register(News, NewsAdmin)
# admin.site.register(News)

for i in [Notices, Academic, Meetings, Relax, Join1, Join2, ]:
    admin.site.register(i, NewsAdmin)


class InlineBase(admin.TabularInline):
    extra = 1


class NestedInlineBase(NestedTabularInline):
    extra = 1


'''
教授相关信息
'''


class ResDirInline(InlineBase):  # 要重启runserver
    model = ResDir


class WorkExpInline(InlineBase):
    model = WorkExp


class PatPriInline(InlineBase):
    model = PatPri


class PubInfInline(InlineBase):
    model = PubInf


class ResActInline(InlineBase):
    model = ResAct


class ProfessorAdmin(admin.ModelAdmin):
    inlines = [ResDirInline, WorkExpInline, PatPriInline, PubInfInline, ResActInline]


admin.site.register(Professor, ProfessorAdmin)

'''
学生相关信息
'''


class ResDirInline1(InlineBase):  # 要重启runserver
    model = ResDir1


class WorkExpInline1(InlineBase):
    model = WorkExp1


class PatPriInline1(InlineBase):
    model = PatPri1


class PubInfInline1(InlineBase):
    model = PubInf1


class ResActInline1(InlineBase):
    model = ResAct1


class PostgraduateAdmin(admin.ModelAdmin):
    inlines = [ResDirInline1, WorkExpInline1, PatPriInline1, PubInfInline1, ResActInline1]


admin.site.register(Postgraduate, PostgraduateAdmin)

'''
实验室相关信息
'''


class ImagesInline(NestedInlineBase):
    model = Images
    # fk_name = "directions"


class DirectionsInline(NestedInlineBase):
    model = Directions
    inlines = [ImagesInline]


class LabAdmin(NestedModelAdmin):
    # modle = Lab
    inlines = [DirectionsInline]


admin.site.register(Lab, LabAdmin)

# for class_i in [WorkExp, ResDir, PatPri, PubInf, ResAct]:
# admin.site.register(class_i)

