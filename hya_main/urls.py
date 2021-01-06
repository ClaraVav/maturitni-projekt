from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.clanek_list, name="clanek_list"),
    url(r'^clanek/(?P<pk>[0-9]+)/$', views.clanek_detail, name="clanek_detail"),
    url(r'^clanek/new/$', views.clanek_new, name="clanek_edit"),
    url(r'^clanek/delete/(?P<pk>[0-9]+)/$', views.clanek_delete, name='clanek_delete'),

    url(r'^prihlaseni/$', views.prihlas, name="prihlaseni"),
    url(r'^registrace/$', views.registr, name="registrace"),
    url(r'^odhlaseni/$', views.user_logout, name="odhlaseni"),

    url(r'^bazos/$', views.bazos, name="bazos"),
    url(r'^internet/$', views.internet, name="internet"),
    url(r'^blox-news/$', views.bloxnews, name="bloxnews"),
    url(r'^instablox/$', views.instablox, name="instablox"),
    url(r'^uredni-deska/$', views.uredka, name="urdeni_deska"),

    url(r'^pravidla/$', views.pravidla, name="pravidla"),
    url(r'^ateam/$', views.ateam, name="ateam"),
    url(r'^galerie/$', views.galerie, name="galerie"),
    url(r'^kontakt/$', views.kontakt, name="kontakt"),

    url(r'^profil/$', views.profil, name="profil"),
    url(r'^postava/(?P<pk>[0-9]+)/$', views.postava_detail, name="postava_detail"),
    url(r'^postava/new/$', views.postava_new, name="postava_new"),
    url(r'^postava/delete/(?P<pk>[0-9]+)/$', views.postava_delete, name='postava_delete'),

    # url(r'^$', views.page_list, name="page_list"),
    url(r'stranky/^(?P<urltitle>[\w\+%_& ]+)/$', views.page_detail, name="page_detail"),
    url(r'^new/$', views.page_new, name="page_new"),
    url(r'^edit/(?P<urltitle>[\w\+%_& ]+)/$', views.page_edit, name="page_edit"),
    url(r'^delete/(?P<urltitle>[\w\+%_& ]+)/$', views.page_delete, name="page_delete"),

    url(r'^chat/$', views.chat, name="chat"),
    url(r'^nova/zprava', views.zprava_new, name="nova-zprava"),
]
