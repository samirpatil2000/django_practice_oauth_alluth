
from django.urls import path
from django import views
from . import views
from.views import PlaylistCreateView,MyView,PublisherList, PublisherBookList,AuthorDetailView,ListView
#
urlpatterns = [
    path('',views.index,name='home'),
    path('play/',PlaylistCreateView.as_view(),name='create'),
    #path('',MyView.as_view(greeting=" G'day "),name='home')
   # path('', PublisherList.as_view()),
  #    path('books/<publisher>/', PublisherBookList.as_view())
    path('books/<publisher>/', PublisherBookList.as_view()),

    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),


    path('tables/',ListView.as_view(),name='tables')
    #path('tables/',views.filter_list,name='tables')


 ]