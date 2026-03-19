from blog import views
from django.urls import path

app_name = 'blog'

# URL dispatcher
# https://docs.djangoproject.com/en/6.0/topics/http/urls/
urlpatterns = [
    path('',  views.blog, name='home'),
    path('<int:post_id>/',  views.post, name='post'),
    path('exemplo/',  views.exemplo, name='exemplo'),
]