from django.db import models
from django.contrib.auth.models import User

class Gym(models.Model):
    class TYPE(models.TextChoices):
        UNISEX = 'Unisex'
        MALE = 'Male'
        FEMALE ='Female',
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=122);
    openingtime=models.TimeField(max_length=122);
    closingtime=models.TimeField(max_length=122);
    address=models.CharField(max_length=122);
    phone=models.CharField(max_length=15);
    city=models.CharField(max_length=122);
    state=models.CharField(max_length=122);
    # interiorimg=models.ImageField(upload_to="GymImg",default="")
    type=models.CharField(max_length=20,choices=TYPE.choices, default=TYPE.UNISEX);
    charge=models.IntegerField();

    

    def __str__(self) :
        return self.name

class Trainer(models.Model):
    class GENDER(models.TextChoices):
        MALE = 'Male'
        FEMALE ='Female',
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
    name=models.CharField(max_length=122);
    age=models.IntegerField();
    gender=models.CharField(max_length=20,choices=GENDER.choices);
    experience=models.IntegerField();
    field=models.CharField(max_length=122);
    phone=models.CharField(max_length=15);
    # certificate=models.ImageField(upload_to="GymImg",default="");
    charge=models.IntegerField();
    
    def __str__(self) :
        return self.name

class Slot(models.Model):
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
    start=models.TimeField(max_length=122);
    end=models.TimeField(max_length=122);
    intake=models.IntegerField(default=0);
    booked=models.IntegerField(default=0);
    slotprice=models.IntegerField(default=100);
    totalprice=models.IntegerField(default=100);
    trainer1=models.CharField(max_length=122,default="")
    trainer2=models.CharField(max_length=122,default="")

    def __str__(self) :
        return str(self.id)


class Client(models.Model):
    class GENDER(models.TextChoices):
        MALE = 'Male'
        FEMALE ='Female',
        
    user=user=models.ForeignKey(User,on_delete=models.CASCADE);
    name=models.CharField(max_length=122);
    gender=models.CharField(max_length=20,choices=GENDER.choices);
    dob=models.DateField();
    phone=models.CharField(max_length=15);
    address=models.CharField(max_length=122);
    def __str__(self) :
        return self.name


class Booking(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE);
    gym=models.ForeignKey(Gym,on_delete=models.CASCADE);
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE);
    amt=models.IntegerField(default=0);
    bookingdate=models.DateTimeField(auto_now_add=True);
    def __str__(self) :
        return str(self.id)

