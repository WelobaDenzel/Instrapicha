from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^accounts/profile/(\d+)', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.get_image_by_id,name ='image'),
    url(r'^new/profile$', views.add_profile, name='add_profile'),
    url(r'^upload$', views.update_image, name='upload'),
    url(r'^comment$', views.add_comment, name='comment')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


    #
