from django.urls import path,include
from . import views

app_name = 'appone'
urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.topiclist, name='topics'),
    path('boards/<int:pk>/newtopic/', views.newtopic, name='newtopic'),
    path('boards/<int:pk>/<int:topic_pk>/', views.postlist, name='topic_posts'),
    path('boards/<int:pk>/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/<int:topic_pk>/<int:post_pk>/edit', views.edit_post, name='edit_post'),

]
