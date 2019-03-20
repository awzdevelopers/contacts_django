from django.shortcuts import render
from app1.models import PhonesTable,ContactsTable




def index(request):
    phones=PhonesTable.objects.all()
    return render(request, 'app1/index.html', context={'ph':phones})


# <<<BY HME>>>


def contactPage(request):
    names = ContactsTable.objects.all()
    return render(request, 'app1/contacts.html', context={'nm':names})
