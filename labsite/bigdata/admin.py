from django.contrib import admin
from bigdata.models import Members
# from labsite.bigdata.models import Members

# class MembersAdmin(admin.ModelAdmin):
#     fields = ['name', 'identity']

# admin.site.register(Members, MembersAdmin)
admin.site.register(Members)