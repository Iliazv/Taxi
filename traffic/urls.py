from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('commentaries/', views.commentaries, name='commentaries'), 
    path('left_order/', views.left_order, name='left_order'),
    path('cars/', views.cars, name='cars'),
    path('left_comment/', views.left_comment, name='left_comment'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('message/', views.message, name='message'),
    path('send_message/', views.send_message, name='send_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)