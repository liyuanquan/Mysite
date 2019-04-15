from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    #url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^$", views.index, name="index"),
    url(r"^(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name="detail"),
    url(r"^(?P<pk>[0-9]+)/result/$", views.ResultsView.as_view(), name="result"),
    url(r"^(?P<pk>[0-9]+)/vote/$", views.vote, name="vote"),

]