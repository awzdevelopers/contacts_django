from django.shortcuts import render
from app1.models import PhonesTable,ContactsTable
from app1.forms import ContactForm,PhoneForm



def index(request):
    phones=PhonesTable.objects.all()
    return render(request, 'app1/index.html', context={'ph':phones})


# <<<BY HME>>>


def contactPage(request):
    # variables intials
    x=""
    contactsInfo=""
    names = ContactsTable.objects.all()

    frm=ContactForm

    if request.method=='POST' and 'sub1' in request.POST:

        frm=ContactForm(request.POST)
        if frm.is_valid():

            frm.save(commit=True)
        else:
            print("ERROR")

    if request.method=='GET' and 'sub2' in request.GET:
        x=request.GET['query1']
        if x:
            contactsInfo=ContactsTable.objects.filter(name=x)
        else:
            contactsInfo=ContactsTable.objects.all()


    names=contactsInfo
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
