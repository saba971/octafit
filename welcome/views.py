import email
from fnmatch import fnmatchcase
#from tkinter import Place
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import pyrebase


#firebase initialize
firebaseConfig = {
  "apiKey": "AIzaSyAipvb7fMXDbG80eF7MBLJYo5colyTpQ60",
  "authDomain": "octafitweb.firebaseapp.com",
  "databaseURL" :"https://octafitweb-default-rtdb.firebaseio.com/",
  "projectId" : "octafitweb",
  "storageBucket": "octafitweb.appspot.com",
  "messagingSenderId": "731631063767",
  "appId": "1:731631063767:web:819b32e43c915aff279692",
  "measurementId": "G-BRX15J7374"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
#global variable
userids=None

def welcomes(request):
    if userids!=None:
        print(userids)
        return render(request,'welcomes.html')
    return render(request,'welcomes.html')

def home(request):
    print(userids)
    if userids!=None:
        return render(request,'home.html')
    else:
       return render(request,'welcomes.html') 


def login(request):
    if request.method == 'POST':
        email=request.POST["email"]
        password=request.POST["password"]
        #sigin user
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            info=auth.get_account_info(user['idToken'])
            for i in info['users']:
                userid=i['email']
            global userids
            userids=userid
            print(userid)
            user={}
            user['name']="Logged in as "+userid
            if not userid:
                user['name']="Not Logged in"
            return render(request,'home.html',{'user':user})
        except:
            return render(request,'login.html')
    return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        email=request.POST["email"]
        password=request.POST["password"]
        #create new user.
        user=auth.create_user_with_email_and_password(email,password)
        return render(request,'login.html')
    return render(request,'signup.html')

def signout(request):
    #auth.signOut()
    print("hi saba")
    auth.current_user = None
    global userids
    userids = None
    print(userids)
    return render(request,'welcomes.html')

def register(request):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
    return render(request,'register.html')

#push to firebase
from .models import client
def clientcount(request):
    if request.method == 'POST':
        name =request.POST["name"]
        age=request.POST["age"]
        place=request.POST["place"]
        phone=request.POST["phone"]
        #firebase will create key for us
        #data={"name":name,"age":age,"place":place,"phone":phone}
        #db.push(data)
        #to create our own key
        data={"name":name,"age":age,"place":place,"phone":phone}
        db.child(phone).set(data)
        return render(request,'count.html')

def view(request):
    return render(request,'view.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def view2(request):
    if request.method == 'POST':
        dict1={}
        phone =request.POST["phone"]
        #to fetch val in db
        detail=db.child(phone).get().val()
        detail=dict(detail)
        print(detail)
        #for user in detail.each():
            #dict1[user.key()]=user.key()
        #print(dict1)
        return render(request,'view2.html',{'details': detail})

def edit1(request):
    if request.method == 'POST':
        name =request.POST["name"]
        age=request.POST["age"]
        place=request.POST["place"]
        phone=request.POST["phone"]
        #To update in db.
        db.child(phone).update({"phone":phone,"name":name,"age":age,"place":place})
        return render(request,'view.html')
    return render(request,'edit1.html')
#sqlite crud
''''
def clientcount(request):
    if request.method == 'POST':
        name =request.POST["name"]
        age=request.POST["age"]
        place=request.POST["place"]
        phone=request.POST["phone"]
        #database save 
        obj=client()
        obj.name=name
        obj.age=age
        obj.place=place
        obj.phone=phone
        obj.save()
        #database retrieve.
        clidata=client.objects.all()
        return render(request,'count.html',{'datas':clidata})
    clidata=client.objects.all()
    return render(request,'count.html',{'datas':clidata})
'''