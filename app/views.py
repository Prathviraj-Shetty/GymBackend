from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.db.models import Q
from app.models import Gym,Client,Slot,Trainer,Booking
from .serializers import GymSerializer,ClientSerializer,TrainerSerializer,SlotSerializer,BookingSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username 
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
     serializer_class=MyTokenObtainPairSerializer

@api_view(['GET'])
def isregistered(request,uid):
    if(len(Client.objects.filter(user=uid))):
        return Response({"regstatus":"Yes"})
    return Response({"regstatus":"No"})

@api_view(['GET'])
def isgymregistered(request,uid):
    print(uid)
    if(len(Gym.objects.filter(user=uid))):
        return Response({"regstatus":"Yes"})
    return Response({"regstatus":"No"})

@api_view(['POST'])
def register(request):
    data=request.data
    type=data['type']
    username=data['username'];
    email=data['email'];
    password=data['password'];
    if(type=="User"): 
        my_user=User.objects.create_user(username,email,password)
    elif(type=="Admin"):
         my_user=User.objects.create_superuser(username,email,password)
    return Response(data)


@api_view(['POST'])
def verifyusername(request):
    data=request.data
    user=len(User.objects.filter(username=data['username']))
    if(user>0):
        return Response({"status":"Yes"})
    return Response({"status":"No"})

@api_view(['GET'])
def usertype(request,uname):
    admin=User.objects.filter(is_superuser=True,username=uname)
    user=User.objects.filter(username=uname)
    if(len(admin)):
        return Response({"type":"Admin"})
    elif(len(user)):
        return Response({"type":"User"})
    return Response({"type":"None"})


@api_view(['GET'])
def searchgym(request):
    if(request.method=='GET'):
        q1=Gym.objects.all()
        serializer=GymSerializer(q1,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def searchgymdynamic(request,str):
    if(request.method=='GET'):
        q1=Gym.objects.all().filter(Q(name__startswith=str)|Q(city__startswith=str)|Q(state__startswith=str))
        serializer=GymSerializer(q1,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getgymdetails(request,id):
    if(request.method=='GET'):
        q1=Gym.objects.all().filter(id=id)
        serializer=GymSerializer(q1,many=True)
        return Response(serializer.data)

   
@api_view(['POST'])
def userprofile(request,str):
    data=request.data;
    user=User.objects.filter(id=data["user"])[0]
    if str=="new":
        Client.objects.create(user=user,name=data['name'],dob=data['dob'],phone=data['phone'],gender=data['gender'],address=data['address'])
    elif str=="update":
        Client.objects.filter(user=user.id).update(name=data['name'],dob=data['dob'],phone=data['phone'],gender=data['gender'],address=data['address'])
    q=Client.objects.last()
    serializer=ClientSerializer(q,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getuserprofile(request,uid):
    client=Client.objects.filter(user=uid)
    serializer=ClientSerializer(client,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def trainerprofile(request):
    data=request.data;
    gym=Gym.objects.filter(user=data["user"])[0]
    print(gym)
    Trainer.objects.create(gym=gym,name=data['name'],age=data['age'],phone=data['phone'],gender=data['gender'],field=data['field'],experience=data['experience'],charge=data['charge'])
    q=Trainer.objects.last()
    serializer=TrainerSerializer(q,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def gymprofile(request,str):
    data=request.data;
    user=User.objects.filter(id=data["user"])[0]
    print(user)
    if str=="new":
        Gym.objects.create(user=user,name=data['name'],type=data['type'],phone=data['phone'],openingtime=data['open'],closingtime=data['close'],charge=data['charge'],address=data['address'],city=data['city'],state=data['state'])
    elif str=="update":
        Gym.objects.filter(user=user.id).update(name=data['name'],type=data['type'],phone=data['phone'],openingtime=data['open'],closingtime=data['close'],charge=data['charge'],address=data['address'],city=data['city'],state=data['state'])
    q=Gym.objects.last()
    serializer=GymSerializer(q,many=False)
    return Response(serializer.data)

   
@api_view(['GET'])
def getgymprofile(request,uid):
    gym=Gym.objects.filter(user=uid)
    serializer=GymSerializer(gym,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getschedule(request,uid):
    gym=Gym.objects.filter(user=uid)[0]
    q1=Slot.objects.filter(gym=gym)
    serializer=SlotSerializer(q1,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getgymschedule(request,gym):
    # gym=Gym.objects.filter(user=uid)[0]
    q1=Slot.objects.filter(gym=gym)
    serializer=SlotSerializer(q1,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addschedule(request):
    data=request.data;
    gym=Gym.objects.filter(user=data['uid'])[0]
    T1charge=Trainer.objects.get(name=data['trainer1']).charge
    T2charge=0
    if(Trainer.objects.filter(name=data['trainer2'])):
        T2charge=Trainer.objects.get(name=data['trainer2']).charge
   
    totalprice=int(data['price'])+T1charge+T2charge
    Slot.objects.create(gym=gym,start=data['start'],end=data['end'],slotprice=data['price'],totalprice=totalprice,intake=data['intake'],trainer1=data['trainer1'],trainer2=data['trainer2'])
    q=Slot.objects.last()
    serializer=SlotSerializer(q,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def gettrainers(request,uid):
    gym=Gym.objects.filter(user=uid)[0]
    q1=Trainer.objects.filter(gym=gym)
    serializer=TrainerSerializer(q1,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def gettrainersdynamic(request,str,uid):
        gym=Gym.objects.filter(user=uid)[0]
        q1=Trainer.objects.all().filter(Q(name__startswith=str),gym=gym)
        serializer=TrainerSerializer(q1,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getgymtrainers(request,gym):
    # gym=Gym.objects.filter(user=uid)[0]
    q1=Trainer.objects.filter(gym=gym)
    serializer=TrainerSerializer(q1,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def bookslot(request):
    data=request.data
    q=Slot.objects.filter(id=data['slotid'])[0]
    if(q.intake<=q.booked):  
        return Response({"status":"full"}) 
    else:
        Slot.objects.filter(id=data['slotid']).update(booked=q.booked+1)
        gym=Gym.objects.get(id=q.gym.id)
        # client=Client.objects.get(user=data['uid'])
        # total_price=q.slotprice+gym.charge
        # Booking.objects.create(client=client,gym=gym,slot=q,amt=total_price)
        # q2=Booking.objects.last()
        # serializer=BookingSerializer(q2,many=False)
        return Response({"status":"notfull"})

@api_view(['GET'])
def getbookingdetail(request,id):
    q=Booking.objects.get(id=id)
    q1=Booking.objects.filter(id=id)
    serializer=BookingSerializer(q1,many=True)
    return Response(serializer.data[0]|{"gymname":q.gym.name,"start":str(q.slot.start)[:5],"end":str(q.slot.end)[:5]})


@api_view(['GET'])
def slotbookings(request,id):
    q=Slot.objects.filter(id=id);
    q1=Booking.objects.filter(slot=id)
    serializer=BookingSerializer(q1,many=True)
    for i in serializer.data:
            s=Client.objects.filter(id=i['client'])
            print(s)
            per=ClientSerializer(s,many=True)
            i["person"]=per.data[0]
    return Response(serializer.data)

@api_view(['GET'])
def delete(request,role,id):
    if(role=="trainer"):
        Trainer.objects.filter(id=id).delete()
    elif(role=="slotbooking"):
        booking=Booking.objects.get(id=id)
        slot=Slot.objects.filter(id=booking.slot.id)
        slot.update(booked=slot[0].booked-1)
        booking.delete()
    return Response({"status":"success"})