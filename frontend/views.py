# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404,redirect
from django.template.response import TemplateResponse
from frontend.forms import SearchForm
from frontend.models import Profile
from django.contrib.auth.models import User


# Create your views here.
def home(request):

	form = SearchForm()
	return render(request, 'home.html', {'form': form})




def results(request):
	form = SearchForm()
	translate_from = request.POST.get('translate_from')
	translate_to = request.POST.get('translate_to')
	results = Profile.objects.filter(translate_from=translate_from,translate_to=translate_to)



	return render(request, 'results.html',{'results':results,'translate_from':translate_from,'translate_to':translate_to,'form': form})




def profile(request, profile_id):
	form = SearchForm()
	profile = get_object_or_404(Profile, pk=profile_id)

	return render(request, 'profile.html',{'profile':profile,'form': form})