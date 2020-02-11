from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Company, Offer

class IndexView(generic.ListView):
	template_name = 'offers/index.html'
	context_object_name = 'latest_offer_list'

	def get_queryset(self):
		"""Return the last five published offers."""
		return Offer.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Offer
	template_name = 'offers/detail.html'

def new_offer(request):
	company_list = Company.objects.all()
	context = {'company_list': company_list}
	return render(request, 'offers/new_offer.html', context)
	
def new_company(request):
	return render(request, 'offers/new_company.html')

def edit(request, pk):
	o = get_object_or_404(Offer, pk=pk)
	company_list = Company.objects.all()
	context = {'company_list': company_list, 'offer': o}
	return render(request, 'offers/edit.html', context)

def save_new(request):
	if request.META['HTTP_REFERER'] == 'http://192.168.56.102:8000/jobz/new/offer/':
		o = Offer(	company=Company.objects.get(pk=request.POST['company']),
					pub_date=timezone.now(),
					location=request.POST['location'],
					offer_title=request.POST['offer_title'],
					offer_text=request.POST['offer_text'])
		o.save()
		return HttpResponseRedirect(reverse('jobz:detail', args=(o.id,)))
	elif request.META['HTTP_REFERER'] == 'http://192.168.56.102:8000/jobz/new/company/':
		c = Company(name=request.POST['name'],
					contact=request.POST['contact'])
		c.save()
		return HttpResponseRedirect(reverse('jobz:index'))
	else:
		return render(request, 'offers/index.html')

def save_edit(request, pk):
	o = get_object_or_404(Offer, pk=pk)
	if request.POST['company']:
		o.company = Company.objects.get(pk=request.POST['company'])
	if request.POST['location']:
		o.location = request.POST['location']
	if request.POST['offer_title']:
		o.offer_title = request.POST['offer_title']
	if request.POST['offer_text']:
		o.offer_text = request.POST['offer_text']
	o.save()
	return HttpResponseRedirect(reverse('jobz:detail', args=(o.id,)))

def delete(request, pk):
	o = get_object_or_404(Offer, pk=pk)
	o.delete()
	return HttpResponseRedirect(reverse('jobz:index'))
