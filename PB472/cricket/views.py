from django.shortcuts import render,redirect,get_object_or_404
from .models import Player

# Create your views here.
def home(req):
    p_list=Player.objects.all()
    return render (req,"home.html",{'players':p_list})

def player_details(req,id):
    p=get_object_or_404(Player,id=id)
    return render (req,"details.html",{'p':p})

def edit_player(req,id):
    p=get_object_or_404(Player,id=id)
    if req.method=='POST':
        p.name=req.POST.get('name')
        p.country=req.POST.get('country')
        p.batting_style=req.POST.get('batting_style')
        p.bowling_style=req.POST.get('bowling_style')
        p.age=req.POST.get('age')
        p.runs=req.POST.get('runs')
        p.wickets=req.POST.get('wickets')

        p.save()
        return redirect('details',id)
    return render(req,'edit.html',{'p':p})

def add_player(req):
    p=Player()
    if req.method=='POST':
        p.name=req.POST.get('name')
        p.country=req.POST.get('country')
        p.batting_style=req.POST.get('batting_style')
        p.bowling_style=req.POST.get('bowling_style')
        p.age=req.POST.get('age')
        p.runs=req.POST.get('runs')
        p.wickets=req.POST.get('wickets')

        p.save()
        return redirect('home')
    return render(req,'add.html')

def delete(req,id):
    p=get_object_or_404(Player,id=id)
    p.delete()
    return redirect('home')
