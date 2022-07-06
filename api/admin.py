from django.contrib import admin
from .models import UserAddress, UserProfile, UserHobby

admin.site.register(UserAddress)
admin.site.register(UserHobby)
admin.site.register(UserProfile)
