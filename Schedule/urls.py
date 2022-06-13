from django.urls import path, re_path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.main_page, name='main_page'),
    # path('', views.LessonFilterView.as_view, name='main_page'),
    # path('filter/', views.filter_page, name='lesson_filter')
]
