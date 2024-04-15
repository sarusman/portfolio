from django.shortcuts import render
from .form import ContactForm
from django.forms.models import model_to_dict
import requests, json, pytz, datetime
from .models import Formation, Projets
from . import mail_engine

mailer=mail_engine.Mail_Engine()

def index(request):
	formation=[model_to_dict(form) for form in Formation.objects.all()]
	projets=[model_to_dict(pro) for pro in Projets.objects.all()]
	mailer.envoyer_email("PORTFOLIO - CONNEXION", "","sarusman.satkunarajah1@gmail.com")
	return render(request, "index.html", {"formation":formation, "projets":projets})

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










