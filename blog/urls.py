from django.urls import path
# <.> it shows that files work with are in the same directory
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # check if there is an integer<int> after <blog/> inside the URL
    path('<int:blog_id>/', views.detail, name='detail'),
]
