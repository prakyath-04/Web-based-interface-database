from django.shortcuts import render

# Create your views here.

# HttpResponse is used to
# pass the information
# back to view

# from django.template import Context, loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from myapp.forms import custforms

# from django.template import loader
# from django.shortcuts import render
# from myapp.models import PmCustmr
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from myapp.forms import SignUpForm
from myapp.models import InsertCustRec,InsertInsurance,InsertHome,InsertDriver,InsertVehicle
# from myapp.models import UpdatePmCustmr
from django.db import connection
from datetime import datetime
from django.urls import path,re_path
from myapp.models import PmCustmr,InsuranceRecord

# Defining a function which
# will receive request and
# perform task depending
# upon function definition
def hello_geek(request):
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello Geeks")

def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({},request))
    return render(request,'index.html')

# def register_request(request):
	# if request.method == "POST":
	# 	form = NewUserForm(request.POST)
	# 	print(form.is_valid())
	# 	if form.is_valid():
	# 		user = form.save()
	# 		login(request, user)
	# 		messages.success(request, "Registration successful." )
	# 		return redirect('/home/')
	# 	else: messages.error(request, "Unsuccessful registration. Invalid information.")
	# form = NewUserForm()
	# return render (request=request, template_name="register.html", context={"register_form":form})
def signup_request(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('login')
	else:
		form = SignUpForm()
	return render(request, 'register.html', {'form': form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/home")

@login_required
def save_record_cust(request):
	if request.method == "POST":
		if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('street') and request.POST.get('house_no') and request.POST.get('city') and request.POST.get('state') and request.POST.get('country') and request.POST.get('zip') and request.POST.get('mart_status'):
			custsave = InsertCustRec()
			custsave.firstname = request.POST.get('firstname')
			if request.POST.get('middlename'):
				custsave.middlename = request.POST.get('middlename')
			else:
				custsave.middlename = None
			custsave.lastname = request.POST.get('lastname')
			custsave.street = request.POST.get('street')
			custsave.house_no = request.POST.get('house_no')
			if request.POST.get('apt_no'):
				custsave.apt_no = request.POST.get('apt_no')
			else:
				custsave.apt_no = None
			custsave.city = request.POST.get('city')
			custsave.state = request.POST.get('state')
			custsave.country = request.POST.get('country')
			custsave.zip = request.POST.get('zip')
			if request.POST.get('gender'):
				custsave.gender = request.POST.get('gender')
			else:
				custsave.gender = None
			custsave.mart_status = request.POST.get('mart_status')
			with transaction.atomic():
				cursor = connection.cursor()
				cursor.callproc('INSERTcustomer',[custsave.firstname,custsave.middlename,custsave.lastname,custsave.street,custsave.house_no,custsave.apt_no,custsave.city,custsave.state,custsave.country,custsave.zip,custsave.gender,custsave.mart_status])
			# pk = cursor.execute("select cid from pm_custmr where fname = %s and lname = %s",[custsave.firstname,custsave.lastname])
			# pk = pk.fetchall()
			# for i in pk:
			# 	id = i
			# id = str(id[0])
			# # messages.success(request,"The customer record "+custsave.firstname+" is saved successfully")

			# return redirect('ins_form/'+id+'')
			return redirect('home')
	else:
		# current_user = request.user
		# print(current_user)
		return render(request,'personal_info.html')


@login_required
def save_insurance(request):
	if request.method == "POST":
		if request.POST.get('cid') and request.POST.get('premium') and request.POST.get('insurance_type'):
			insave = InsertInsurance()
			insave.cid = request.POST.get('cid')
			insave.insurance_type = request.POST.get('insurance_type')
			insave.premium = request.POST.get('premium')
			insave.status = "C"

			temp = datetime.now().date()
			insave.startdate = temp

			temp = request.POST.get('enddate')
			insave.enddate = temp
			with transaction.atomic():
				cursor = connection.cursor()
				cursor.callproc('InsertInsurance',[insave.insurance_type,insave.premium,insave.status,insave.startdate,insave.enddate,insave.cid])

			return redirect('home')
	else:
		return render(request,'insurance_form.html')

@login_required
def save_vehicle(request):
	if request.method == "POST":
		if request.POST.get('vin') and request.POST.get('vmake') and request.POST.get('vmodel') and request.POST.get('model_yr') and request.POST.get('status') and request.POST.get('ins_no'):
			vsave = InsertVehicle()
			vsave.vin = request.POST.get('vin')
			vsave.vmake = request.POST.get('vmake')
			vsave.vmodel = request.POST.get('vmodel')
			vsave.model_yr = request.POST.get('model_yr')
			vsave.status = request.POST.get('status')
			vsave.ins_no = request.POST.get('ins_no')
			with transaction.atomic():
				cursor = connection.cursor()
				cursor.callproc('InsertVehicle',[vsave.vin,vsave.vmake,vsave.vmodel,vsave.model_yr,vsave.status,vsave.ins_no])

			return redirect('home')
	else:
		return render(request,'vehicle_form.html')

@login_required
def save_driver(request):
	if request.method == "POST":
		if request.POST.get('licence') and request.POST.get('d_fname') and request.POST.get('d_lname') and request.POST.get('birthdate') and request.POST.get('vin'):
			dsave = InsertDriver()
			dsave.licence = request.POST.get('licence')
			dsave.d_fname = request.POST.get('d_fname')
			dsave.d_lname = request.POST.get('d_lname')
			if request.POST.get('d_mname'):
				dsave.d_mname = request.POST.get('d_mname')
			else:
				dsave.d_mname = None
			dsave.birthdate = request.POST.get('birthdate')
			dsave.vin = request.POST.get('vin')
			with transaction.atomic():
				cursor = connection.cursor()
				cursor.callproc('InsertDriver',[dsave.licence,dsave.d_fname,dsave.d_lname,dsave.d_mname,dsave.birthdate,dsave.vin])

			return redirect('home')
	else:
		return render(request,'driver_form.html')

@login_required
def save_home(request):
	if request.method == "POST":
		if request.POST.get('pur_date') and request.POST.get('pur_value') and request.POST.get('area') and request.POST.get('htype') and request.POST.get('auto_fire_n') and request.POST.get('home_security') and request.POST.get('basement') and request.POST.get('ins_no'):
			hsave = InsertHome()
			hsave.pur_date = request.POST.get('pur_date')
			hsave.pur_value = request.POST.get('pur_value')
			hsave.area = request.POST.get('area')
			hsave.htype = request.POST.get('htype')
			hsave.auto_fire_n = request.POST.get('auto_fire_n')
			hsave.home_security = request.POST.get('home_security')
			hsave.basement = request.POST.get('basement')
			if request.POST.get('swim_pool'):
				hsave.swim_pool = request.POST.get('swim_pool')
			else:
				hsave.swim_pool = None
			hsave.ins_no = request.POST.get('ins_no')
			with transaction.atomic():
				cursor = connection.cursor()
				cursor.callproc('InsertHome',[hsave.pur_date, hsave.pur_value, hsave.area, hsave.htype, hsave.auto_fire_n, hsave.home_security, hsave.basement, hsave.swim_pool, hsave.ins_no])

			return redirect('home')
	else:
		return render(request,'home_form.html')

@login_required
def get_customer_record(request):
	if request.method == "POST":
		if request.POST.get('firstname') and request.POST.get('lastname'):
			cursor = connection.cursor()
			cursor.execute('Select * from pm_custmr where fname = %s and lname = %s',[request.POST.get('firstname'),request.POST.get('lastname')])
			data = cursor.fetchall()
			print(data[0][1])
			return render(request,'record.html',{"PmCustmr":data})
	else:
		return render(request,'name.html')

@login_required
def get_insurance_record(request):
	if request.method == "POST":
		if request.POST.get('firstname') and request.POST.get('lastname'):
			cursor = connection.cursor()
			cursor.execute('Select cid from pm_custmr where fname = %s and lname = %s',[request.POST.get('firstname'),request.POST.get('lastname')])
			pk = cursor.fetchall()
			for i in pk:
				id = i
			id = int(id[0])
			print(id)
			cursor.execute('select * from (select * from pm_insrnce a join (select b.start_date,b.end_date,b.cid,b.ins_no from pm_cust_insr b join pm_custmr c on b.cid = c.cid where c.cid = %s) d on a.ins_no=d.ins_no) ',[id])
			data = cursor.fetchall()
			print(data)
			return render(request,'ins_record.html',{"InsuranceRecord":data})
	else:
		return render(request,'name.html')

@login_required
def get_all_customers(request):
	cursor = connection.cursor()
	cursor.execute('Select * from pm_custmr')
	data = cursor.fetchall()
	# print(data[0][1])
	return render(request,'record.html',{"PmCustmr":data})

@login_required
def get_all_insurance(request):
	cursor = connection.cursor()
	cursor.execute('select * from (select * from pm_insrnce a join (select b.start_date,b.end_date,b.cid,b.ins_no from pm_cust_insr b join pm_custmr c on b.cid = c.cid) d on a.ins_no=d.ins_no) ')
	data = cursor.fetchall()
	# print(data[0][1])
	return render(request,'ins_record.html',{"InsuranceRecord":data})

@login_required
def update_cust(request):
	if request.method == "POST":
		if request.POST.get('firstname') and request.POST.get('lastname'):
			cursor = connection.cursor()
			cursor.execute('Select * from pm_custmr where fname = %s and lname = %s',[request.POST.get('firstname'),request.POST.get('lastname')])
			pk = cursor.fetchall()
			for i in pk:
				id = i
			id = int(id[0])
			data = PmCustmr.objects.get(cid=id)
			print(data)
			return render(request,'update_customer.html',{"PmCustmr":data})
	else:
		return render(request,'name.html')

@login_required
def update_cust_db(request):
	id = int([i for i in str(request.path).split('/') if i][-1])
	cust = PmCustmr.objects.get(cid = id)
	form = custforms(request.POST,instance=cust)
	if form.is_valid:
		form.save()
		return render(request,'update_customer.html',{"PmCustmr":cust})


@login_required
def delete_cust_record(request):
	if request.method == "POST":
		if request.POST.get('firstname') and request.POST.get('lastname'):
			cursor = connection.cursor()
			cursor.callproc('DeleteCustomer',[request.POST.get('firstname'),request.POST.get('lastname')])
			return redirect('home')
	else:
		return render(request,'name.html')

@login_required
def get_invoice(request):
	if request.method == "POST":
		if request.POST.get('ins_no'):
			cursor = connection.cursor()
			cursor.execute('Select * from pm_invoice where ins_no = %s',[request.POST.get('ins_no')])
			data = cursor.fetchall()
			return render(request,'invoice.html',{"PmInvoice":data})
	else:
		return render(request,'ins_no.html')