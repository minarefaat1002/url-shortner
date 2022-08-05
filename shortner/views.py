from django.http import HttpResponse
from django.shortcuts import render,redirect
import uuid
from .models import Url
# Create your views here.


def index(request):
    return render(request, 'index.html')
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        urlId = str(uuid.uuid4())[:5]
        new_url = Url(link=link,urlId=urlId)
        new_url.save()
        return HttpResponse(urlId)
def go(request,pk):
    url_details = Url.objects.get(urlId = pk)
    if url_details.link[0:4]=="http":
        return redirect(url_details.link)
    return redirect('https://' + url_details.link)