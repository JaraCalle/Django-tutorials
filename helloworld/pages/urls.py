from django import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
