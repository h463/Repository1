from django.conf.urls import url

from . import views

app_name = "recipe_app"
urlpatterns=[
    url(r'^$', views.login_view, name="login_view"),
    url(r'^register/$', views.register, name="register"),
    url(r'^home/$', views.home, name="home"),
    url(r'^create/$', views.create, name="create"),
    url(r'^save_recipe/$', views.save_recipe, name="save_recipe"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^(?P<recipe_id>[0-9]+)/detail/$', views.detail, name="detail"),
    url(r'^(?P<recipe_id>[0-9]+)/delete/$', views.delete, name="delete"),
]