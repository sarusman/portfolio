from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ContactForm
from django.forms.models import model_to_dict
import requests, json, pytz, datetime
from datetime import timedelta
from .models import Formation, Projets
from . import mail_engine
import requests, ast

mailer=mail_engine.Mail_Engine()

def index(request):
	formation=[model_to_dict(form) for form in Formation.objects.all()]
	projets=[model_to_dict(pro) for pro in Projets.objects.all()]
	response=render(request, "index.html", {"formation": formation, "projets": projets})
	print(request.COOKIES)
	if "abuse" in request.COOKIES:
		va=int(request.COOKIES["abuse"])
		if va>5:
			return redirect("https://www.youtube.com/watch?v=NGGoulSNeIs")
		else:
			response.set_cookie('abuse', str(va+1), expires=datetime.datetime.now()+timedelta(hours=3)) # ADAPTATION SERVEUR (TIMEZONE DIFFÉRENT (+2H))
			try:
				mailer.envoyer_email("PORTFOLIO - CONNEXION", "","sarusman.satkunarajah1@gmail.com")
			except:
				pass
	else:
		response.set_cookie('abuse', '0', expires=datetime.datetime.now()+timedelta(hours=3)) # ADAPTATION SERVEUR (TIMEZONE DIFFÉRENT (+2H))
		try:
			mailer.envoyer_email("PORTFOLIO - CONNEXION", "","sarusman.satkunarajah1@gmail.com")
		except:
			pass

	return response

def checker(request):
	return HttpResponse("iOBtt5U4fsQBzb2L5SSsIlkVQ1AQ2G9cyJTcorkwbGY.dKu2rqEOe0s1P47nC55iSK0ZHklTZpOnEByxLSVTeZg")

def license(request):
	return render(request, "license.html")


def contact(request):
	if request.method == 'POST':
		nom=request.POST.get('nom', '')
		contact=request.POST.get('contact', '')
		message=request.POST.get('message', '')
		message=f"Message de : {nom} \n Message : {message} \n Contact : {contact}"
		mailer.envoyer_email("PORTFOLIO - MESSAGE", message, "sarusman.satkunarajah1@gmail.com")
	return index(request)


def btc(request):
	res=ast.literal_eval(requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text)
	print(res["bpi"]["EUR"])









