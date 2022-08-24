from django.shortcuts import render, redirect
from docsApp.forms import DocumentForm
from docsApp.models import Document


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('choose_file')
    else:
        form = DocumentForm()

        context = {
            'form': form,
        }
    return render(request, 'docsApp/upload_file.html', context)


def retrieve_files(request):
    all_files = Document.objects.all()
    context = {
        'all_files': all_files,
    }
    return render(request, 'docsApp/home.html', context)
