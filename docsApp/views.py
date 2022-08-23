from django.shortcuts import render


def choose_file(request):
    return render(request, 'docsApp/home.html')


def upload_file(request):
    return render(request, 'docsApp/upload_file.html')
