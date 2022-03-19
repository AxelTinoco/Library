from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



# Create your models here.

class Library(models.Model):
    name = models.TextField()
    adress = models.TextField()

    def getAdress(self):
        return self.adress

    def __str__(self):
        return f'Name : [ {self.name} ] Adress : [{self.adress}]'


class Librarian(models.Model):
    def addBookItem(self):
        return bool

    def blockMember(self):
        return bool

    def unblockMember(self):
        return bool


class Member(models.Model):
    date_of_membership = models.DateField()
    total_books_checkedout = models.IntegerField()

    def getTotalCheckedOutBooks(self):
        return self.total_books_checkedout


class Account(models.Model,Member,Librarian):
    id = models.TextField()
    password = models.TextField()

    # status = AccountStatus
    # person = Person

    def resetPassword(self):
        self.password = ""
        return bool

class BookReservation(models.Model):
    creation_date = models.DateField
    #status = ReservationStatus

    def getStatus(self):
        return self.status

    def fetchReservationDetails(self):
        return BookReservation


class BookLending(models.Model):
    creation_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()

    def getReturnDate(self):
        return self.return_date

class Fine(models.Model):
    amount = models.FloatField()

    def getAmount(self):
        return self.amount


class FineTransaction(models.Model):
    creation_date = models.DateField()
    amount = models.FloatField()

    def initiateTransaction(self):
        return bool

class CreditCardTransaction(models.Model):
    name_on_card = models.TextField()

class CheckTransaction(models.Model):
    bank_name = models.TextField()
    check_number = models.TextField()

class CashTransaction(models.Model):
    cash_tendered = models.FloatField()

class LibraryCard(models.Model):
    card_number = models.TextField()
    barcode = models.TextField()
    issued_at = models.DateTimeField()
    active = models.BooleanField()

class BarcodeReader(models.Model):
    id = models.TextField()
    registered_at = models.DateField()

    def isActive(self):
        return bool


class BookItem(models.Model):
    barcode = models.TextField()
    is_reference_only = models.BooleanField(default= False)
    borrowed = models.DateTimeField()
    due_date = models.DateTimeField()
    price = models.FloatField()
    # format = BookFormat
    # status = BookStatus
    date_of_purchase = models.DateField()
    publication_date = models.DateField()

    def checkout(self):
        return bool


class Rack(models.Model):
    number = models.IntegerField()
    location_identifier = models.CharField(max_length=255)




class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


    def getName(self) -> str:
        return self.name


class Catalog(models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    totalBooks = models.IntegerField()
    bookTitles = ArrayField(models.CharField(max_length=100, blank=False))
    bookAuthors = ArrayField(models.CharField(max_length=100, blank=False))
    bookSubjects = ArrayField(models.CharField(max_length=100, blank=False))
    bookPublicationDate = ArrayField(models.DateField(auto_now_add=True))


    def updateCatalog(self) -> bool:
        return True



# class PostalNotification(models.Model):
    # address = Address
 

class EmailNotification(models.Model):
    email = models.EmailField()


# class Notification(models.Model, EmailNotification, PostalNotification):
#     notificationid = models.IntegerField()
#     createdOn = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(max_length=500)


#     def sendNotification(self)-> bool:
#         return True
    