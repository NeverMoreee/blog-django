from django.shortcuts import render

# Create your views here.

from .models import Message
import datetime

def index(request):
    ms_list = Message.objects.order_by('-ms_pub_date')
    context = {'ms_list': ms_list}
    return render(request, 'message/index.html', context)
def add(request):
    ms_title = request.GET['title']
    ms_content = request.GET['content']
    Message.objects.create(ms_title=ms_title, ms_content= ms_content, ms_pub_date=datetime.datetime.now())
    return index(request)