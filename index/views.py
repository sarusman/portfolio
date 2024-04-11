from django.shortcuts import render
from django.forms.models import model_to_dict
import requests, json, pytz, datetime
from .models import Formation, Projets

def index(request):
	formation=[model_to_dict(form) for form in Formation.objects.all()]
	projets=[model_to_dict(pro) for pro in Projets.objects.all()]
	client_ip="PRIVATE LOG POUR VOIR"
	#rep=eval(requests.get(f"https://ipinfo.io/{client_ip}/json").text.replace("true", "True").replace("false", "False"))
	rep={"ip":client_ip}
	fr_timezone = pytz.timezone('Europe/Paris')
	current_time_fr =datetime.datetime.now(fr_timezone).strftime('%Y-%m-%d %H:%M:%S')
	rep["date"]=current_time_fr
	requests.get("https://serveur.pythonanywhere.com/cool/poper/"+json.dumps(rep))
	return render(request, "index.html", {"formation":formation, "projets":projets})

def log(request):
	data=eval(requests.get("https://serveur.pythonanywhere.com/see/see").text)
	for i in  range(len(data)):
		try:
			data[i]=eval(data[i].replace("true", "True").replace("false", "False"))
		except:
			pass
	print(data)
	return render(request, "index/log.html",{"data":data})
	

def checker(request):
	return HttpResponse("iOBtt5U4fsQBzb2L5SSsIlkVQ1AQ2G9cyJTcorkwbGY.dKu2rqEOe0s1P47nC55iSK0ZHklTZpOnEByxLSVTeZg")