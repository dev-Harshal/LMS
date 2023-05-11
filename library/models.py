from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
import uuid 

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    prn_no = models.IntegerField(unique=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    branch = models.CharField(max_length=100,null=True,blank=True) 

    def __str__(self):
        return str(self.prn_no) + " : " + self.user.first_name + " " + self.user.last_name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    
    choice = (('Education', 'Education'),('Entertainment', 'Entertainment'),
              ('Computer Science', 'Computer Science'),('Physics', 'Physics'),('Mathematics', 'Mathematics'))

    category = models.CharField(max_length=100, choices=choice)

    def __str__(self):
        return self.title

class BookInstance(models.Model):
    isbn=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Book unique id across the Library")
    book=models.ForeignKey(Book, on_delete=models.CASCADE,null=True)         
    Is_borrowed = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.isbn}  :  {self.book}"
    

def get_returndate():
    return datetime.today() + timedelta(days=8)
    
class Book_Issue(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True,help_text="Date the book is issued")
    due_date = models.DateTimeField(default=get_returndate(),help_text="Date the book is due to")

    def __str__(self):
        return self.borrower.first_name + " borrowed " + self.book_instance.book.title

