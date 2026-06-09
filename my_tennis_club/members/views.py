from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members_first(request):
    # template = loader.get_template("myfirst.html")
    # return HttpResponse(template.render())
    return render(request, "myfirst.html")

def members(request):
    members = Member.objects.all().values()
    # template = loader.get_template("all_members.html")
    context = {
        "members": members,
    }
    return render(request, "all_members.html", context)

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'member': mymember,
  }
  return HttpResponse(template.render(context, request))