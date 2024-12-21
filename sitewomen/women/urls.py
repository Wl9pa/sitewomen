from django.urls import path, re_path, register_converter
from django.views.decorators.cache import cache_page

from . import views
from . import converters

register_converter(converters.FourDigitYearConverters, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPost.as_view(), name='add_page'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTag.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='edit_page'),
]
