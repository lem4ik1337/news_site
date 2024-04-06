from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import RegisterView, NewsDetailView

urlpatterns = [
    path('', TemplateView.as_view(template_name="main/index.html"), name='index'),
    path('news/',  views.news, name='news'),
    path('news/creation/', views.create_view, name='creation_news'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='detail_news'),
    #path('new_user/', views.new_user, name='new_user'),
    path('new_date/', views.new_date, name='new_date_name'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_user/<slug:cat>', views.new_user_slug, name='new_user_slug')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)