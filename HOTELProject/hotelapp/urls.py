from django.urls import path
from .import views
from django.conf.urls import url
urlpatterns =[
    path("", views.home_view),
    path("category/", views.category_view),
    path("normal/", views.normal_rooms_view),
    #path("normal/(?P<id>\d+)/", views.normal_rooms_view),
    path("ac/", views.ac_rooms_view),
    path("vip/", views.vip_rooms_view),
    path("signup/", views.signup_view),
    path("details/", views.customer_detail_view),
    #url(r"^details/(?P<pk>\d+)/$", views.customer_detail_view),
    path("logout/", views.logout_view),
]