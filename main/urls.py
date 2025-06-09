from django.urls import include, path
from .views import home
from main import views

urlpatterns = [
    path('', home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('feed', views.all_posts, name='feed'),
    path('controller/<int:year>/', views.gamming_controller_detail, name='controller_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('listar-sites/', views.listar_sites),
]