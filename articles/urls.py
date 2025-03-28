"""
URL configuration for board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # C
    path('create/', views.create, name='create'),

    # R
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # U
    path('<int:id>/update/', views.update, name='update'),
    # D
    path('<int:id>/delete/', views.delete, name='delete'),

    # Comment
    # C
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    
    # Delete
    path('<int:article_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete')
]
