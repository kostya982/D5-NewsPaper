from django.urls import path
from . import views
from .views import ProductsList


urlpatterns = [
   path('news/', views.news_list, name='news_list'),
   path('news/<int:news_id>/', views.news_detail, name='news_detail'),
   path('', ProductsList.as_view()),
]