from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume


def home(request):
    if request.POST:
        r = Resume()
        r.title = request.POST.get("title")
        r.skill = request.POST.get("skill")
        r.content = request.POST.get("content")
        r.save()
        return redirect("resumes:home")
    resumes = Resume.objects.all()
    return render(request, "resumes/home.html", {"resumes": resumes})


def new(request):
    return render(request, "resumes/new.html")


def show(request, id):
    resumes = get_object_or_404(Resume, id=id)
    if request.POST:
        resumes.title = request.POST.get("title")
        resumes.skill = request.POST.get("skill")
        resumes.content = request.POST.get("content")
        resumes.save()
        return redirect("resumes:home")
    return render(request, "resumes/show.html", {"resumes": resumes})


def edit(request, id):
    resumes = get_object_or_404(Resume, id=id)
    return render(request, "resumes/edit.html", {"resumes": resumes})


def delete(request, id):
    resumes = get_object_or_404(Resume, id=id)
    if request.POST:
        resumes.delete()
        return redirect("resumes:home")
    return render(request, "resumes/delete.html", {"resumes": resumes})


# Create your views here.
