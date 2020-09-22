from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
from django.conf.urls import url, include
from django.urls import path
from .views import ArticleCreateSerik, ArticleDeleteSerik, ArticleListSerik, UserCreateSerik, UserListViewSerik


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.ArticleListView.as_view(), name='articles'),
    # url(r'article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name='article-detail'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
    url(r'article/like/(?P<pk>\d+)/$', views.OnlikeView.as_view(), name='article-up'),
    url('user/create/', views.CreateUserView.as_view(), name='create_user'),
    url(r'article/comment/delete/(?P<comment_id>\d+)/$', views.DeleteComment.as_view(), name='delcomment'),
    url(r'article/comment/create/(?P<art_id>\d+)/$', views.AddComment.as_view(), name='addcomment'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/articles/list', ArticleListSerik.as_view()),
    path('api/articles/create/', ArticleCreateSerik.as_view()),
    path('api/articles/<int:pk>', ArticleDeleteSerik.as_view()),
    path('api/articles/register/', UserCreateSerik.as_view()),
    path('api/articles/user/list', UserListViewSerik.as_view()),



]

urlpatterns += [
    url(r'^article/(?P<pk>[-\w]+)/renew/$', views.renew_art_staff, name='renew-article-staff'),
]
urlpatterns += [
    url(r'^article/create/$', views.ArticleCreateView.as_view(), name='article_create'),
    url(r'^article/update/(?P<pk>\d+)/update/$', views.ArticleUpdateView.as_view(), name='article_update'),
    url(r'^article/delete/(?P<pk>\d+)/delete/$', views.ArticleDeleteView.as_view(), name='article_delete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
