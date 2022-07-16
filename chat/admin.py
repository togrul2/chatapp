from django.contrib import admin

from chat.models import Friendship, Message, Chat

admin.site.register(Friendship)
admin.site.register(Message)
admin.site.register(Chat)
