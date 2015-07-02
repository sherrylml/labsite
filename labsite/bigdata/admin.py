from django.contrib import admin
# from labsite.bigdata.models import Members

# class MembersAdmin(admin.ModelAdmin):
# fields = ['name', 'identity']

# admin.site.register(Members, MembersAdmin)
from bigdata.models import Members, Notation, Team, News, LearningMaterials, JoinUs

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp']

admin.site.register(Members)
admin.site.register(Team)
admin.site.register(Notation)
admin.site.register(News, NewsAdmin)
# admin.site.register(News)
admin.site.register(LearningMaterials)
admin.site.register(JoinUs)
