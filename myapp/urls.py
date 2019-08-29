from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path('', views.index),
    # path('index/', views.index),
    # path('<int:question_id>/', views.details, name = "detail"),
    path('<int:question_id>/', views.details, name='detail'),
    path('<int:question_id>/results/', views.results, name= "result"),
    path('<int:question_id>/votes/', views.votes, name= "vote"),
]