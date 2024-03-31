from django.urls import path
from .views import HomePage, GetRequestView, PostRequestView, GetResponseView
urlpatterns = [
    path('get/', HomePage.as_view(), name="homepage"),
    path('get/request/', GetRequestView, name='home'),
    path('post/request/', PostRequestView),
    path('get/response/', GetResponseView),
    
]