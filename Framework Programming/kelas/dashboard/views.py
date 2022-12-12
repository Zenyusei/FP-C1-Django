from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang
from dashboard.models import Member

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Member_View(request):
    members=Member.objects.all()

    konteks={
        'members':members,
    }
    return render(request,'member.html',konteks)

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def store(request):
    titlenya="store"
    konteks = {
        'title':titlenya,
    }
    return render(request,'store.html',konteks
    )

def pay(request):
    titlenya="pay"
    konteks = {
        'title':titlenya,
    }
    return render(request,'pay.html',konteks
    )

def item(request):
    titlenya="item"
    konteks = {
        'title':titlenya,
    }
    return render(request,'item.html',konteks
    )

def about(request):
    titlenya="about"
    konteks = {
        'title':titlenya,
    }
    return render(request,'about.html',konteks
    )

def daftar(request):
    titlenya="daftar"
    konteks = {
        'title':titlenya,
    }
    return render(request,'daftar.html',konteks
    )

def login(request):
    titlenya="login"
    konteks = {
        'title':titlenya,
    }
    return render(request,'login.html',konteks
    )

def member(request):
    titlenya="member"
    konteks = {
        'title':titlenya,
    }
    return render(request,'member.html',konteks
    )