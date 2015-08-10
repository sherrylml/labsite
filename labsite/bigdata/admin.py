from django.contrib import admin
from .models.models import *
from .models.team_models import *
from .models.Englishmodels import *
from .models.EnglishTeam_models import *
from nested_inline.admin import NestedModelAdmin, NestedTabularInline


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']

# admin.site.register(News, NewsAdmin)

for i in [News, Notices, Academic, Meetings, Relax, Join1, Join2, ]:
    admin.site.register(i, NewsAdmin)

for i in [NewsEn, NoticesEn, AcademicEn, MeetingsEn, RelaxEn, Join1En, Join2En, ]:
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
English 教授信息
'''
class ResDirEnInline(InlineBase):  # 要重启runserver
    model = ResDirEn


class WorkExpEnInline(InlineBase):
    model = WorkExpEn


class PatPriEnInline(InlineBase):
    model = PatPriEn


class PubInfEnInline(InlineBase):
    model = PubInfEn


class ResActEnInline(InlineBase):
    model = ResActEn


class ProfessorEnAdmin(admin.ModelAdmin):
    inlines = [ResDirEnInline, WorkExpEnInline, PatPriEnInline, PubInfEnInline, ResActEnInline]


admin.site.register(ProfessorEn, ProfessorEnAdmin)


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
English
'''
class ResDirEnInline1(InlineBase):  # 要重启runserver
    model = ResDir1En


class WorkExpEnInline1(InlineBase):
    model = WorkExp1En


class PatPriEnInline1(InlineBase):
    model = PatPri1En


class PubInfEnInline1(InlineBase):
    model = PubInf1En


class ResActEnInline1(InlineBase):
    model = ResAct1En


class PostgraduateEnAdmin(admin.ModelAdmin):
    inlines = [ResDirEnInline1, WorkExpEnInline1, PatPriEnInline1, PubInfEnInline1, ResActEnInline1]


admin.site.register(PostgraduateEn, PostgraduateEnAdmin)



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
'''
English
'''

class ImagesEnInline(NestedInlineBase):
    model = ImagesEn
    # fk_name = "directions"


class DirectionsEnInline(NestedInlineBase):
    model = DirectionsEn
    inlines = [ImagesEnInline]


class LabEnAdmin(NestedModelAdmin):
    # modle = Lab
    inlines = [DirectionsEnInline]


admin.site.register(LabEn, LabEnAdmin)