from django.urls import path
from . import views

urlpatterns = [
    # path('<int:pk>/', views.single_post_page), #FBV 형식일 때 
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('', views.index), #FBV 형식일 때 
    path('', views.PostList.as_view())
]

