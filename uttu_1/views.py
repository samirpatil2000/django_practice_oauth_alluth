from django.http import HttpResponse
from django.shortcuts import render,reverse
from django.utils import timezone
from django.views import View

from .models import  Area, Place,Song,Playlist,Publisher,Book,Author,Apk_file,MyModel
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView






# Create your views here.

def index(request):
    place = Place.objects.all()
    apk_file=Apk_file.objects.all()
    #areas = place.area.all()

    context = {
        "places": place,
        'files':apk_file,
       # "areas": areas,
    }
    return render(request,'uttu_1/index.html',context)

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['name','owner','songs']
    def get_success_url(self):
        return reverse('home')



# def my_view(request):
#     if request.method == 'GET':
#         # <view logic>
#      return HttpResponse('result')

class MyView(View):
    greeting = "Good Day"
    def get(self,request):
        return HttpResponse(self.greeting)

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'



class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'uttu_1/acme_list.html'


class PublisherBookList(ListView):
    template_name = 'uttu_1/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj



# For Table Testing

from django_tables2 import SingleTableView
from .tables import MyTable

class ListView(SingleTableView):
    model=MyModel
    table_class=MyTable
    template_name='uttu_1/tables.html'


# for filtering
def filter_list(request):
    context=MyModel.objects.all()
    statusCode="No"
    table_class=MyTable
    filterContext_=MyModel.objects.filter(status=statusCode)
    filterContext={
        'table':filterContext_,
    }
    template_name='uttu_1/tables.html'
    return render(request,template_name,filterContext)














