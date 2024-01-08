from django.shortcuts import render,redirect
from .models import user,customer_detail
from django.http import HttpResponse
def register(request):
    if request.method == "POST":
        username = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        new_register = user.objects.create(username=username,firstname=firstname,lastname=lastname,email=email,mobile_number=mobile,password=password)
                
    return render(request,"register.html")
def login(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user_data = list(user.objects.all().values())
        # print(user_data)
        new_user = list(user.objects.filter(password=password,username=username).values())
        if username == "admin" and password =="admin1234":
            return redirect('http://127.0.0.1:8000/create_customer/')
        else:
            for i in user_data:
                    try:
                        username = new_user[0]['username']
                        user_password = new_user[0]['password']
                        if username == i['username'] and password == i['password']: 
                            return redirect('http://127.0.0.1:8000/create_customer/')
                    except:
                        return HttpResponse('username or password is invalid')
            
    return render(request,"login.html")
def create_customer(request):
    if request.method == "POST":
        customerName = request.POST['custname']
        customerAddress = request.POST['custaddr']
        custNumber = request.POST['custmobile']
        new_customer = customer_detail.objects.create(customer_name=customerName,customer_number=custNumber,customer_address=customerAddress)
        
    return render(request,'admin.html')
def customerDetails(request):
    customerdetails = customer_detail.objects.all().values()
    return render(request,'customer_details.html',context={"customer_detail":customerdetails})



