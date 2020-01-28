from rest_framework.permissions import BasePermission

class verify_following(BasePermission):
    def has_permission(self,request,view,obj):
        return obj.user in request.user.profile.following()

class IsOwner(BasePermission):
    def has_permission(self,request,view,obj):
        return obj.user == request.user
