from django.contrib import admin
from .models import *
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'typeContent', 'date', 'uuid')

    #def userinfo(self, obj):
        #return obj.user.username

    def queryset(self, request):
        qs = super(ContentAdmin, self).get_queryset(request)
        qs = qs.order_by('date')
        return qs

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'repliedUser', 'contentid')

    def repliedUser(self, obj):
        return obj.ParentContent.user.username

    def contentid(self, obj):
        return obj.ParentContent.uuid

#admin.site.register(Content, ContentAdmin)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Content)
admin.site.register(QPost)
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(Like)
