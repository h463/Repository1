from django.conf.urls import url

from . import views

app_name = "rest_api"
urlpatterns = [

    url(r'^$', views.login_view, name="login_view"),
    url(r'^home/$', views.home, name="home"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.register, name="register"),
    url(r'^create_recipe/$',views.create_recipe, name="create_recipe"),
    url(r'^save_recipe/$', views.save_recipe, name="save_recipe"),
    url(r'^(?P<recipe_id>[0-9]+)/detail/$', views.detail, name="detail"),
    url(r'^(?P<recipe_id>[0-9]+)/delete/$', views.delete, name="delete"),
]