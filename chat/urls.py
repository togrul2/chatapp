from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('chat/<int:receiver_id>/', views.chat_view, name='chat'),
    path('friends/', views.friends_view, name='friends'),
    path('friendship-requests/', views.friend_requests, name='friend-requests'),
    path('accept/<int:request_id>/', views.accept_request, name='accept-request'),
    path('decline/<int:request_id>/', views.decline_request, name='decline-request'),
    path('find-friends/', views.find_friends, name='find-friends'),
    path('send-friendship-request/<int:pk>/', views.send_friendship_request, name='send_friendship_request')
]
