from django.shortcuts import render , HttpResponse ,redirect
from.models import employee , Tenantname , Mainmeter , Submeter , Tankerentry 
from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, "index.html")

def login(request):
    return render(request,"login.html")

def registration(request):
    return render(request,"registration.html")

def register(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        e=employee(fname=fname,lname=lname,email=email,password=password)
        e.save()    #insert....

        return redirect("index")
    else:
        return HttpResponse("Fail")

def login_check(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        data= employee.objects.all().filter(email=email,password=password)

        if len(data)==1:

            request.session["username"]=email

            for d in data:
                request.session["name"]=d.fname

            return redirect("index")
        else:
            return redirect("login")

def logout(request):
    del request.session["username"]
    del request.session["name"]
    return redirect("login")


# /////////////  Register Tenant start \\\\\\\\\\\\\\\


def add(request):
    if request.session.get('username') is not None:
       a = request.session.get('username')
       data1 = employee.objects.all().filter(email=a)
       return render(request, "add.html",{'data1':data1})
    else:
        return redirect("login")

def register_tenant(request):
     if request.method=="POST":
        FlatNumber = request.POST["FlatNumber"]
        name = request.POST["name"]
        Address = request.POST["Address"]
        Adhar = request.POST["Adhar"]
        rent = request.POST["rent"]
        phone = request.POST["phone"]

        time = datetime.now()
        todaysdate=time.strftime("%Y-%m-%d")
        
        messages.success(request,"Registration Successfully Completed")
        s = Tenantname(FlatNumber=FlatNumber , name=name ,Address=Address , Adhar=Adhar , rent=rent , phone=phone , todaysdate=todaysdate)
        s.save()
        
        return redirect("index")
     else:
        return HttpResponse("fail")

def Modify(request):
    id  = request.GET['id']
    data1 = Tenantname.objects.all().filter(id=id)  # edit
    return render(request, "Modify.html" , {'data1':data1})

def update_data(request):
    if request.method=="POST":
        id = request.POST['id']
        FlatNumber = request.POST["FlatNumber"]
        name = request.POST["name"]
        Address = request.POST["Address"]
        Adhar = request.POST["Adhar"]
        rent = request.POST["rent"]
        phone = request.POST["phone"]

        Tenantname.objects.filter(id=id).update(FlatNumber=FlatNumber , name=name ,Address=Address , Adhar=Adhar , rent=rent , phone=phone)

        return redirect("Tenant_Entry")
    else:
        return redirect("Tenant_Entry")
    
# /////////////  Register Tenant End \\\\\\\\\\\\\\\
    
    
# /////////////// Main Meter Entry start //////////////

def meter_entry(request):
    if request.session.get('username') is not None:
        a = request.session.get('username')
        data = employee.objects.all().filter(email=a)
        return render(request, "meter_entry.html",{'data':data})
    else:
       return redirect("login")
    
def mainmeter(request):
    if request.method=="POST":
        meterNo = request.POST["meterNo"]
        month = request.POST["month"]
        year = request.POST["year"]
        unitConsumed = request.POST["unitConsumed"]
        amount = request.POST["amount"]


        time = datetime.now()
        todaysdate=time.strftime("%Y-%m-%d")
        
        s = Mainmeter(meterNo=meterNo , month=month ,year=year , unitConsumed=unitConsumed , amount=amount , todaysdate=todaysdate)
        s.save()

        return redirect("M_Meter_Report")
    else:
        return redirect("meter_entry")


def mainmeter_edit(request):
    id  = request.GET['id']
    data = Mainmeter.objects.all().filter(id=id)  # edit
    return render(request, "mainmeter_edit.html" , {'data':data})

def Update_Mainmeter(request):
    if request.method=="POST":
        id = request.POST['id']
        meterNo = request.POST["meterNo"]
        month = request.POST["month"]
        year = request.POST["year"]
        unitConsumed = request.POST["unitConsumed"]
        amount = request.POST["amount"]

        Mainmeter.objects.filter(id=id).update(meterNo=meterNo , month=month ,year=year , unitConsumed=unitConsumed , amount=amount)

        return redirect("M_Meter_Report")
    else:
        return redirect("mainmeter_edit")
    
# //////////// Main Meter Entry end \\\\\\\\\\\\\\\\\\



# ////////////// Sub Meter Entry start \\\\\\\\\\\\\\

def sub_meter(request):
    if request.session.get('username') is not None:
        a = request.session.get('username')
        data2 = employee.objects.all().filter(email=a)
        return render(request, "sub_meter.html",{'data2':data2})
    else:
       return redirect("login")

def submeter(request):
     if request.method=="POST":
        tenantName = request.POST["tenantName"]
        meterID = request.POST["meterID"]
        previousReading = request.POST["previousReading"]
        currentReading = request.POST["currentReading"]
        amount = request.POST["amount"]

        time = datetime.now()
        todaysdate=time.strftime("%Y-%m-%d")
        
        s = Submeter(tenantName=tenantName, meterID=meterID , previousReading=previousReading , currentReading=currentReading , amount=amount , todaysdate=todaysdate)
        s.save()
        
        return redirect("S_Meter_Report")
     else:
        return HttpResponse("sub_meter")

def submeter_edit(request):
    id  = request.GET['id']
    data2 = Submeter.objects.all().filter(id=id)  # edit
    return render(request, "submeter_edit.html" , {'data2':data2})

def Update_Submeter(request):
    if request.method=="POST":
        id = request.POST['id']
        tenantName = request.POST["tenantName"]
        meterID = request.POST["meterID"]
        previousReading = request.POST["previousReading"]
        currentReading = request.POST["currentReading"]
        amount = request.POST["amount"]


        Submeter.objects.filter(id=id).update(tenantName=tenantName, meterID=meterID , previousReading=previousReading , currentReading=currentReading , amount=amount)

        return redirect("S_Meter_Report")
    else:
        return redirect("submeter_edit")

# ////////////// Sub Meter Entry End \\\\\\\\\\\\\\\



# /////////////  Tanker Entry start \\\\\\\\\\\\\\\

def tanker_entry(request):
    if request.session.get('username') is not None:
        a = request.session.get('username')
        data3 = employee.objects.all().filter(email=a)
        return render(request, "tanker_entry.html",{'data3':data3})
    else:
       return redirect("login")
    
def tanker_data(request):
     if request.method=="POST":
        month = request.POST["month"]
        year = request.POST["year"]
        totalTanker = request.POST["totalTanker"]
        amtPerTanker = request.POST["amtPerTanker"]
        numOfTenants = request.POST["numOfTenants"]

        time = datetime.now()
        todaysdate=time.strftime("%Y-%m-%d")
        
        s = Tankerentry(month=month, year=year , totalTanker=totalTanker , amtPerTanker=amtPerTanker , numOfTenants=numOfTenants , todaysdate=todaysdate)
        s.save()
        
        return redirect("Tanker_Report")
     else:
        return HttpResponse("tanker_data")

def tanker_data_edit(request):
    id  = request.GET['id']
    data3 = Tankerentry.objects.all().filter(id=id)  # edit
    return render(request, "tanker_data_edit.html" , {'data3':data3})

def Update_Tanker(request):
    if request.method=="POST":
        id = request.POST['id']
        month = request.POST["month"]
        year = request.POST["year"]
        totalTanker = request.POST["totalTanker"]
        amtPerTanker = request.POST["amtPerTanker"]
        numOfTenants = request.POST["numOfTenants"]

        Tankerentry.objects.filter(id=id).update(month=month, year=year , totalTanker=totalTanker , amtPerTanker=amtPerTanker , numOfTenants=numOfTenants)

        return redirect("Tanker_Report")
    else:
        return redirect("tanker_data_edit")
    
# /////////////  Tanker Entry End \\\\\\\\\\\\\\\


# /////////////  Report Start \\\\\\\\\\\\\\\

    
def Tenant_Entry(request):
    if request.session.get('username') is not None:
        data1 = Tenantname.objects.all()   #select
        return render(request,"Tenant_Entry.html" , {'data1': data1})
    else:
        return redirect("login")

def showresults(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')

        serachresults = Tenantname.objects.raw('select id,FlatNumber,name,Address,Adhar,rent,phone,todaysdate from myapp_tenantname where todaysdate between "'+fromdate+'" and "'+todate+'"')
        return render(request,'Tenant_Entry.html',{'data1':serachresults})
    else:
        displaydata=Tenantname.objects.all()
        return render(request,'Tenant_Entry.html',{'data1': displaydata})

    
def M_Meter_Report(request):
    if request.session.get('username') is not None:
        data = Mainmeter.objects.all()   #select
        return render(request,"M_Meter_Report.html" , {'data':data})
    else:
        return redirect("login")
    
def showMeterResults(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')

        serachresults = Tenantname.objects.raw('select id,meterNo,month,unitConsumed,amount,year,todaysdate from myapp_mainmeter where todaysdate between "'+fromdate+'" and "'+todate+'"')
        return render(request,'M_Meter_Report.html',{'data':serachresults})
    else:
        displaydata=Tenantname.objects.all()
        return render(request,'M_Meter_Report.html',{'data': displaydata})

    
def S_Meter_Report(request):
    if request.session.get('username') is not None:
        data2 = Submeter.objects.all()   #select
        return render(request,"S_Meter_Report.html" , {'data2':data2 })
    else:
        return redirect("login")

def Show_Sub_MeterResults(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')

        serachresults = Tenantname.objects.raw('select id,tenantName,meterID,previousReading,currentReading,amount,todaysdate from myapp_Submeter where todaysdate between "'+fromdate+'" and "'+todate+'"')
        return render(request,'S_Meter_Report.html',{'data2':serachresults})
    else:
        displaydata=Tenantname.objects.all()
        return render(request,'S_Meter_Report.html',{'data2': displaydata})
    
def Tanker_Report(request):
    if request.session.get('username') is not None:
        data3 = Tankerentry.objects.all()   #select
        return render(request,"Tanker_Report.html" , {'data3':data3})
    else:
        return redirect("login")
    
def Show_Tanker_Results(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')

        serachresults = Tenantname.objects.raw('select id,month,year,totalTanker,amtPerTanker,numOfTenants,todaysdate from myapp_Tankerentry where todaysdate between "'+fromdate+'" and "'+todate+'"')
        return render(request,'Tanker_Report.html',{'data3':serachresults})
    else:
        displaydata=Tenantname.objects.all()
        return render(request,'Tanker_Report.html',{'data3': displaydata})


# /////////////  Report Start \\\\\\\\\\\\\\\

   
def delete(request):
     id = request.GET['id']
     Tenantname.objects.filter(id=id).delete()  # delete
     return redirect("Tenant_Entry")

def delete_Mainmeter(request):
     id = request.GET['id']
     Mainmeter.objects.filter(id=id).delete()  # delete
     return redirect("Tenant_Entry")

def delete_Submeter(request):
     id = request.GET['id']
     Submeter.objects.filter(id=id).delete()  # delete
     return redirect("Tenant_Entry")

def delete_Tanker(request):
     id = request.GET['id']
     Tankerentry.objects.filter(id=id).delete()  # delete
     return redirect("Tenant_Entry")


    