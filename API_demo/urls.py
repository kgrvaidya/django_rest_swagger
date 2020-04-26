from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProjectsList.as_view()),
    path('<int:pk>', views.ProjectDetail.as_view()),
    path('floors/', views.FloorsList.as_view()),
    path('floors/blobs', views.BlobDetail.as_view()),

]
