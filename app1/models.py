from django.db import models

# Create your model
class ContactsTable(models.Model):
    name=models.CharField(max_length=256)
    family=models.CharField(max_length=256)
    job=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PhonesTable(models.Model):
    contacts=models.ForeignKey(ContactsTable,on_delete=models.CASCADE)
    MobilePhoneNo=models.CharField(max_length=20)
    IsInWhatsapp=models.BooleanField()
    IsInTelegram=models.BooleanField()
    IsInInstagram=models.BooleanField()
    sHomePhoneNo=models.CharField(max_length=20)
    sWorkPhoneNo=models.CharField(max_length=20)
