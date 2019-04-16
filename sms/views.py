from django.shortcuts import render
from django.contrib import auth
from django.template import Template, Context
import requests




def home(request):
    #commingsoon
    

    return render(request,"login.html")


    #######################################################################
def authenticateusers(request):
    #This is user authentication section
    #Authenticate or Validate users login data
	username = request.POST.get("username")
	password = request.POST.get("password")
	r = requests.post('https://swaq-sms-hub-api.herokuapp.com/authenticate', json={"email" : username, "password" : password})
	try:
		
		if r:
			res = r.json()
			print(r.json())
			response = res['response']
			message = res['message']
			if response == "True":
				return render(request,"admin_dashboard.html", {"message":message})
			elif response == "False":
				return render(request,"login.html", {"message":message})
	except Exception as e:
		raise e 
	
	message = "Cannot authenticate you. Try again."
	
	

    

	return render(request,"login.html", {"message":message})
    #-----------------------------


