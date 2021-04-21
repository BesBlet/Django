from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render


from .models import News

def index(request):
	lastest_news_list = News.objects.all().order_by('-pub_date')
	return render(request, 'list.html', {'lastest_news_list': lastest_news_list})

def detail(request, news_id):
	try:
		a = News.object.get( id = news_id)
	except:
		raise Http404("Новость не найдена")
	return render(request, 'detail.html', {'news': a})

def hunar(request):
	return render(request, 'hunar.html')
def contacts(request):
	return render(request, 'contacts.html')
def galereya(request):
	return render(request, 'galereya.html')
def talyplara(request):
	return render(request, 'talyplara.html')
