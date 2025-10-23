from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='details'),
    path('post/new/', views.post_create, name='create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # ✅ add this
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # ✅ add this
]
