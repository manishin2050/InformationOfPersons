from django.shortcuts import render,redirect
from Main.models import Data,Video
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


# code for home page--------------------------------------------
def index(request):
    content={
        "data":Data.objects.order_by('id'),
        "users":User.objects.all().values()
    }
    # data ko different different way me dikahne ke liyeee
    return render(request,'index.html',content)


# code for add data in base --------------------------------------------
def AddData(request):
    if request.method=="POST":
        # img file hai ya url check karne ke liyee --
        img=request.FILES.get('fimg')

        if img == None:
            img=request.POST.get('img')


        name=request.POST.get('name')
        category=request.POST.get('category')
        desc=request.POST.get('desc')
        fb=request.POST.get('fb')
        youtube=request.POST.get('youtube')
        insta=request.POST.get('insta')
        google=request.POST.get('google')
        tdate=date.today()

        data=Data(img=img,name=name,desc=desc,category=category,fb=fb,youtube=youtube,insta=insta,google=google,tdate=tdate)
        data.save()
    return render(request,'addData.html')


# code for update html page----------------------------------------------------
def Update(request,id):
    datas={
        "id":id,
        "name":Data.objects.get(id=id).name,
        "category":Data.objects.get(id=id).category,
        "desc":Data.objects.get(id=id).desc,
        "fb":Data.objects.get(id=id).fb,
        "insta":Data.objects.get(id=id).insta,
        "youtube":Data.objects.get(id=id).youtube,
        "google":Data.objects.get(id=id).google,
        "img":Data.objects.get(id=id).img
    }

    if request.method=="POST":
        # img file hai ya url check karne ke liyee --
        img=request.FILES.get('fimg')
        if img == None:
            img=request.POST.get('img')

        name=request.POST.get('name')
        category=request.POST.get('category')
        desc=request.POST.get('desc')
        fb=request.POST.get('fb')
        youtube=request.POST.get('youtube')
        insta=request.POST.get('insta')
        google=request.POST.get('google')
        # tdate=date.today()
        # agar img nhi hai same img hogi ---
        imgs=Data.objects.get(id=id).img
        if img  == None or img == '':
            data=Data(id=id,img=imgs,name=name,desc=desc,category=category,fb=fb,youtube=youtube,insta=insta,google=google)
            data.save()

        else:
            # agar img me image hai to pehle wali delete ho jayegi
            if imgs !='static/imgs/1.jpeg':
                imgs.delete()
                print("delete ho gyi")
            data=Data(id=id,img=img,name=name,desc=desc,category=category,fb=fb,youtube=youtube,insta=insta,google=google)
            data.save()
        return redirect('/')
    return render(request,'update.html',datas)


# code for about------------------------------------------------------
def About(request,id):
    datas={
        "id":id,
        "name":Data.objects.get(id=id).name,
        "category":Data.objects.get(id=id).category,
        "desc":Data.objects.get(id=id).desc,
        "fb":Data.objects.get(id=id).fb,
        "insta":Data.objects.get(id=id).insta,
        "youtube":Data.objects.get(id=id).youtube,
        "google":Data.objects.get(id=id).google,
        "img":Data.objects.get(id=id).img,
        "videos":Video.objects.order_by('-id').filter(code=id),
        "path":"https://www.youtube.com/embed/"
    }

    return render(request,'about.html',datas)


# code for to add video -------------------------------------------------
def AddVideo(request,id):
    if request.method=="POST":
        url=request.POST.get('url')
        code=id
        title=request.POST.get('title')
        # url se id alg karne ke liye
        if "?v=" in url:
            url=url.split('=')[-1]
        elif "shorts/" in url:
            url=url.split('/')[-1]

        elif ".be/" in url:
            url=url.split('.be/')[-1]

            url=url.split('?si=')[0]


        Video(url=url,code=code,title=title).save()

    return render(request,"addVideo.html",{'id':id})


# Code for editVideo html page ---------------------------------------------------------
def editVideo(request,id):
    video={
        "url":Video.objects.get(id=id).url,
        "code":Video.objects.get(id=id).code,
        "title":Video.objects.get(id=id).title
    }
    if request.method=="POST":
        url=request.POST.get('url')
        code=request.POST.get('code')
        title=request.POST.get('title')
        # youtube ke video yha se play hogi
        if "?v=" in url:
            url=url.split('=')[-1]
        elif "shorts/" in url:
            url=url.split('/')[-1]

        elif ".be/" in url:
            url=url.split('.be/')[-1]

            url=url.split('?si=')[0]

        aboutPage=Video.objects.get(id=id).code
        Video(id=id,url=url,code=code,title=title).save()
        return redirect(f'/about/{aboutPage}')

    return render(request,"editVideo.html",video)

def deleteVideo(request,id):
    code=Video.objects.get(id=id).code
    Video.objects.get(id=id).delete()
    return redirect(f'/about/{code}')


# code for login user ----------------------------------------------------
def Log_in(request):
    if request.method=="POST":
        username=request.POST.get('username')
        # username="admin"
        password=request.POST.get('password')
        # password="admin"
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/')
    return redirect('/')

# code for sign up user-------------------------------------------
def sign_up(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password == cpassword:
            myuser=User.objects.create_user(username=username,password=password)
            # myuser.set_password(password)
            myuser.save()

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')

        else:
            return redirect('/')
    return redirect('/')


# code for logout user ----------------------------------------------------
def Log_out(request):
    if request.method=="POST":
        logout(request)
    return redirect('/')


# Code for play Add Free Video ------------------------------------------------

def playAddFreeVideo(request):
    if request.method=="GET":
        url= request.GET.get('url')
        # this code is so powerful it can play video using link like[share link, video id,etc..]
        if "?v=" in url:
            url=url.split('=')[-1]
        elif "shorts/" in url:
            url=url.split('/')[-1]

        elif ".be/" in url:
            url=url.split('.be/')[-1]

            url=url.split('?si=')[0]


    return render(request,'playAddFreeVideo.html',{"url":url})


# ------------------------------------------------------- Special Feautres Area ------------------------------------------


# code for category page------------
def category(request):
    if request.method=="GET":
        value=request.GET.get('cate')
    return render(request,'category.html',{"data":Data.objects.filter(category__icontains=value)})


# code for search page------------
def search(request):
    if request.method=="GET":
        value=request.GET.get('cate')
    return render(request,'index.html',{"data":Data.objects.filter(name__icontains=value)|Data.objects.filter(category__icontains=value)|Data.objects.filter(desc__icontains=value)})


# code for payment
def payment(request,id):
    import random
    city=['Mumbai','Kolkata','Delhi','Chennai','Goa','Hariyana','London','New York']
    context={
        "id":id,
        "img":Data.objects.get(id=id).img,
        "name":Data.objects.get(id=id).name,
        "category":Data.objects.get(id=id).category,
        "price":random.randint(10,50),
        "city":random.choice(city),

    }
    return render(request,'paypal.html',context)