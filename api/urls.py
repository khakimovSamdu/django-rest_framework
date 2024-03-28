from django.urls import path
from .views import HomePage, home
urlpatterns = [
    path('get/', HomePage.as_view(), name="homepage"),
    path('home/', home, name='home'),
    
]