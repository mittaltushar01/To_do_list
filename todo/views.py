from django.shortcuts import render
from .models import todoitem
from django.http import HttpResponseRedirect
# Create your views here.
def todoview(request):
    alltodoitems = todoitem.objects.all()
    return render(request,'todo.html',{'allitems':alltodoitems})

def additem(request):
    newitem = todoitem(content=request.POST['content'])
    newitem.save()
    return HttpResponseRedirect('/todo/')

def deleteitem(request,itemid):
    item=todoitem.objects.get(id=itemid)
    item.delete()
    return HttpResponseRedirect('/todo/')
