from django.shortcuts import render
from app1.models import PhonesTable,ContactsTable




def index(request):
    phones=PhonesTable.objects.all()
    return render(request, 'app1/index.html', context={'ph':phones})


# <<<BY HME>>>


def contactPage(request):
    names = ContactsTable.objects.all()
    return render(request, 'app1/contacts.html', context={'nm':names})

def contactPage(request):
    names = ContactsTable.objects.all()
    return render(request, 'app1/contactlist.html', context={'nm':names})

def numberPage(request):
    numbers = PhonesTable.objects.all()
    return render(request, 'app1/contactlist.html', context={'nu':numbers})