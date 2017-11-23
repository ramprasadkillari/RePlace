#for basic rendering of html pages
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

#for authentication login and logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from student.models import *
from replace.models import *


import datetime

HOME_URL = '/'

def auth(user):
	return Company.objects.filter(user=user).exists()

def get_company(user):
	return Company.objects.get(user = user)

@login_required()
def logout(request):
	if (auth(request.user)):
		auth_logout(request)
	return redirect(HOME_URL)

@login_required()
def home(request):
	if (not auth(request.user)):
		return redirect(HOME_URL)
	company = get_company(request.user)	
	jaf_list = JAF.objects.filter(company = company)
	for jaf in jaf_list:
		jaf.student_count  = Application.objects.filter(jaf = jaf).count()
	data = {"jaf_list":jaf_list}
	return render(request, "company/home.html", context = data)

@login_required()
def new_jaf(request):
	if (not auth(request.user)):
		return redirect(HOME_URL)
	if request.method == "POST" :
		company = get_company(request.user)
		profile_name = request.POST.get("profile")
		description = request.POST.get("description")
		requirements = request.POST.get("requirements")
		posting = request.POST.get("posting")
		resume_type = request.POST.get("resume_type")
		job_season = request.POST.get("job_season")
		year = request.POST.get("year")
		duration = request.POST.get("duration")
		accommodation = request.POST.get("accommodation")
		other_details = request.POST.get("other_details")
		cpi_cutoff = request.POST.get("cpi_cutoff")
		stipend = request.POST.get("stipend")
		currency = request.POST.get("currency")
		eligibility_list = request.POST.getlist("eligibility_list")
		deadline_date = request.POST.get("deadline_date")
		deadline_time = request.POST.get("deadline_time")
		test_type_name = request.POST.getlist("test_type")
		test_duration = request.POST.getlist("test_duration")
		test_description = request.POST.getlist("test_description")
		test_length = len(test_type_name)
		profile = JobProfile.objects.get(name = profile_name)
		print (job_season)
		jaf = JAF(company = company, description = description, profile = profile, other_details = other_details, accomodation = accommodation)
		jaf.requirements = requirements
		jaf.resume_number = resume_type
		jaf.job_year = int(year)
		jaf.job_season = int(job_season)
		jaf.duration = float(duration)
		jaf.cpi_cutoff = float(cpi_cutoff)
		jaf.stipend = float(stipend)
		jaf.currency = currency
		jaf.posting = posting
		jaf.deadline = datetime.datetime.now()
		jaf.save()
		print (eligibility_list)
		for eligibility_data in eligibility_list:
			department_name,program_name = eligibility_data.split("-")
			department = Department.objects.get(name = department_name)
			program = Program.objects.get(name = program_name)
			eligibility = Eligibility(jaf = jaf, department = department, program = program)
			eligibility.save()
		for i in range(0,test_length):
			test_type = TestType.objects.get(type = test_type_name[i])
			jaftest = JAFTest(jaf = jaf, test_number = i+1, test_type = test_type, duration = float(test_duration[i]), description = test_description[i])
			jaftest.save()
		return redirect("/company/")
	else :
		resume_type_list = Resume._meta.get_field("resume_number").choices
		job_profile_list = JobProfile.objects.all()
		program_list = Program.objects.all()
		department_list = Department.objects.all()
		test_type_list = TestType.objects.all()
		data = {'job_profile_list':job_profile_list,
		'resume_type_list':resume_type_list,
		'program_list':program_list,
		'department_list':department_list,
		'test_type_list':test_type_list}
		return render(request, "company/jaf_form.html", context=data )