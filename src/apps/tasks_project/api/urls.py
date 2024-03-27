from django.urls import path

from . import views


urlpatterns = (
    path('custom/', views.UserTaskCustomListAV.as_view()),
    path('custom/get_reward/', views.TaskCustomGetRewardAV.as_view()),
)
