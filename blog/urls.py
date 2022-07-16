from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogsView.as_view(), name="blogs"),
    path('create/', views.blog_create_view, name="create_blog"),
    path('subscribe/', views.CreateSubscriptionView.as_view(), name='subscribe'),
    path('<slug:slug>/', views.BlogView.as_view(), name="blog"),
]
