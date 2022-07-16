from django.contrib import admin

from blog.models import Blog, Subscription

admin.site.register(Blog)
admin.site.register(Subscription)
