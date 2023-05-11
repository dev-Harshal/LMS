from django.urls import path
from . views import index,home,viewAll,addBook,bookInstance,issueBook,viewIssuedBooks,profile


app_name = 'library'

urlpatterns = [
    path('',index,name='index'),
    path('home/',home,name='home'),
    path('viewAll',viewAll,name="viewAll"),
    path('addBook/',addBook,name="addBook"),
    path('bookInstance/',bookInstance,name="bookInstance"),
    path('issueBook/',issueBook,name="issueBook"),
    path('issuedBooks/',viewIssuedBooks,name="issuedBooks"),
    path('profile/<int:id>/<int:bk_id>/',profile,name="profile"),
]
