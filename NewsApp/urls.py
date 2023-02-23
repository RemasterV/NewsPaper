from django.urls import path
from .views import News, News_search, New, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', News.as_view()),
   path('search/', News_search.as_view()),
   path('<int:pk>', New.as_view()),
   path('create/', PostCreate.as_view()),
   path('<int:pk>/update/', PostUpdate.as_view()),
   path('<int:pk>/delete/', PostDelete.as_view()),
]
