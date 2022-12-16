from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('list/', views.list_view, name='list'),
    path('<id>/', views.detail_view, name='detail'),
    path('<id>/update/', views.update_view, name='update'),
    path('<id>/delete/', views.delete_view, name='delete')
]