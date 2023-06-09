from django.urls import path, re_path
from . import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.canvas, name='canvas'),

    # The home page
    path('', views.index, name='index'),
]