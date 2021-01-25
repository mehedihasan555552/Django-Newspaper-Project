from django.contrib import admin
from . models import *
# Register your models here.

# from django_summernote.admin import SummernoteModelAdmin


# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)




admin.site.register(LatestPost)



admin.site.register(User)

admin.site.site_title = "Mehedi Blog"
admin.site.site_header = "Mehedi Blog"
admin.site.index_title = "Mehedi Blog"
