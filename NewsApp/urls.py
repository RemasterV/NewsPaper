from django.urls import path
from .views import News, News_search, New, PostCreate, PostUpdate, PostDelete, CategoryListView,subscribe
from django.views.decorators.cache import cache_page
urlpatterns = [
   path('', cache_page(60)(News.as_view())),
   path('search/', News_search.as_view()),
   path('<int:pk>', cache_page(60*5)(New.as_view())),
   path('create/', PostCreate.as_view()),
   path('<int:pk>/update/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]
