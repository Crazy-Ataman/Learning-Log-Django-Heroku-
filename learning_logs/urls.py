"""Defines URL schemes for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage.
    path('', views.index, name='index'),
    # Page with a list of all topics.
    path('topics/', views.topics, name='topics'),
    # Page with the detailed information on a particular topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    # Page for deleting entry.
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]