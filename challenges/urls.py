from django.urls import path 
from . import views


urlpatterns = [
    path('', views.ChallengeListView.as_view(), name='challenge_list'),
    path('challenge/new/', views.challenge_new, name='challenge_new'),
]
