from django.shortcuts import render

def about_me(request):
    return render(request, 'about_me.html')

def experience(request):
    return render(request, 'experience.html')

def education(request):
    return render(request, 'education.html')

def skills(request):
    return render(request, 'skills.html')
