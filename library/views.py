from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .models import Book,BookInstance,Book_Issue
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('library:home')
        else:
            return render(request,'library/index.html')
    else:
        return render(request,'library/index.html')
    
def home(request):
    return render(request,'library/home.html')

    
def viewAll(request):
    books = Book.objects.all()
    return render(request,'library/viewAll.html',context={'books':books})


def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')

        Book.objects.create(title=title, author=author, category=category)
        return redirect('library:home')
    else:
        return render(request,'library/addBook.html')
    
def bookInstance(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST.get('book'))
        Is_borrowed = request.POST.get('Is_borrowed')

        if Is_borrowed == None:
            Is_borrowed = False

        BookInstance.objects.create(book=book, Is_borrowed=Is_borrowed)
        return redirect('library:home')
    else:
        books = Book.objects.all()
        return render(request,'library/bookInstance.html',context={'books':books})
    
def issueBook(request):
    if request.method == 'POST':
        borrower = User.objects.get(id=request.POST.get('borrower'))
        book_instance = BookInstance.objects.get(isbn=request.POST.get('isbn'))
        Book_Issue.objects.create(borrower=borrower,book_instance=book_instance)
        return redirect('library:home')
    else:
        users = User.objects.all()
        book_instances = BookInstance.objects.filter(Is_borrowed=False).all()
        return render(request,'library/issueBook.html',context={'book_instances':book_instances,'users':users})
    

def viewIssuedBooks(request):
    issued_books = Book_Issue.objects.all()
    return render(request,'library/issuedBooks.html',context={'issued_books':issued_books})

def profile(request,id,bk_id):
    user = User.objects.get(id=id)
    books = Book_Issue.objects.get(id=bk_id)
    return render(request,'library/profile.html',context={'user':user, 'books':books})
