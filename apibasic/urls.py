from rest_framework.urlpatterns import format_suffix_patterns
from apibasic import views
from django.urls import path
from .views import *
from rest_framework import renderers

renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('article/',article_list),
    path('detail/<int:pk>',article_detail),
    path('articlelist/',article_listApiview),
    path('detailapiview/<int:pk>',article_detailapiview),
    path('articellistclassapi',views.ArticleListClassview.as_view()),
    path('articledetailsclassapi/<int:pk>',views.ArticleDetailClassview.as_view()),
    path('articellistMixinapi', views.ArticleListMixins.as_view()),
    path('articledetailmixinapi/<int:pk>', views.ArticaldetailMixins.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('login', views.UserLoginView.as_view()),
    path('usersviewset/', views.UserViewSet.as_view()),


]
urlpatterns = format_suffix_patterns(urlpatterns)