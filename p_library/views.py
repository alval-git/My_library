from django.shortcuts import render
from p_library.models import author, book, WhoAndWhatTook
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.forms import formset_factory  
from p_library.forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.views.generic import FormView  
from allauth.socialaccount.models import SocialAccount 
from django.contrib.auth import authenticate  

# Create your views here.
def Book_list(request):
	books = book.objects.all()
	return HttpResponse(books)


def index(request):

    template  = loader.get_template('index.html')
    books = book.objects.all()
    biblio_data = {'title': 'мою библиотеку',
                    'books': books,
                    }
    if request.user.is_authenticated:
        biblio_data['username'] = request.user.username
    return HttpResponse(template.render(biblio_data, request))



def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            any_book = book.objects.filter(id=book_id).first()
            if not any_book:
                return redirect('/index/')
            any_book.copy_count += 1
            any_book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            any_book = book.objects.filter(id=book_id).first()
            if not any_book:
                return redirect('/index/')
            if any_book.copy_count < 1:
                any_book.copy_count = 0
            else:
                any_book.copy_count -= 1
            any_book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')
def PublishHouse(request): 
    template = loader.get_template('publish_house.html')
    books = book.objects.all()
    biblio_data = {'books':books}
    return HttpResponse(template.render(biblio_data))
def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm,extra=2)
    if request.method == "POST":
        author_formset = AuthorFormSet(request.POST,request.FILES,prefix='authors')
        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))
    else:
        author_formset = AuthorFormSet(prefix='authors')
    return render(request, 'manage_authors.html', {'author_formset': author_formset})
class AuthorEdit(CreateView):  
    model = author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'author_edit.html'  
class AuthorList(ListView):  
    model = author  
    template_name = 'author_list.html'

def WhoTook(request):
    template = loader.get_template('friends_books.html')
    friends_books = WhoAndWhatTook.objects.all()
    biblio_data = {'friends_books':friends_books}
    return HttpResponse(template.render(biblio_data, request))

    
