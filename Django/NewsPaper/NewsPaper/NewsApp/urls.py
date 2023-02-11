from django.urls import path
from .views import News, News_search, New, CreatePost, PostUpdate, PostDelete

urlpatterns = [
   path('', News.as_view()),
   path('search/', News_search.as_view()),
   path('<int:pk>', New.as_view()),
   path('create/', CreatePost),
   path('<int:pk>/update/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
]
