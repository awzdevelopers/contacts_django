from django.shortcuts import render
from app1.models import PhonesTable,ContactsTable
from app1.forms import ContactForm,PhoneForm



def index(request):
    phones=PhonesTable.objects.all()
    return render(request, 'app1/index.html', context={'ph':phones})



# <<<BY HME>>>


def contactPage(request):
    frm=ContactForm
    if request.method=='POST':
        frm=ContactForm(request.POST)
        if frm.is_valid():
            frm.save(commit=True)
        else:
            print("ERROR")

    names = ContactsTable.objects.all()
    return render(request, 'app1/contacts.html', context={'nm':names,'frm':frm})

# def contactPage(request):
#     names = ContactsTable.objects.all()
#     return render(request, 'app1/contactlist.html', context={'nm':names})

def numberPage(request):
    frm=PhoneForm
    if request.method=='POST':
        frm=PhoneForm(request.POST)
        if frm.is_valid():
            frm.save(commit=True)

    numbers = PhonesTable.objects.all()
    return render(request, 'app1/contactlist.html', context={'nu':numbers,'frm':frm})
