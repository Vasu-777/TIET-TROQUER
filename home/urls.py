from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name="home"),
    path('feeds/',								feeds_home,			name='feeds'),
    path('feed-details/<int:pk>',				feed_details,		name='feed_details'),
    path('my/feeds/', 							my_post, 			name='my_feeds'),
    path('delete/feed/<int:id>/', 				delete_feed,		name='delete_feed'),
    path('update/feed/<int:id>/', 				update_feed,		name='update_feed'),
    path('delete/comment/<int:pk>/',            delete_comment,     name='delete-comment'),
]
