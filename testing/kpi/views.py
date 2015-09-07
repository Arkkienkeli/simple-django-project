from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import Kpi, Aim, Term


@login_required(login_url='/accounts/login/')
def kpi(request):
	user = request.user
	terms = Term.objects.filter(user=user)
	for term in terms:
		term.kpis = Kpi.objects.filter(dates=term)
		term.date = str(term.date)[:7]
		term.term = str(term.term)[:7]
		for kpi in term.kpis:
			kpi.aims = Aim.objects.filter(kpi=kpi)
	return render_to_response('kpi.html', {'terms':terms })

