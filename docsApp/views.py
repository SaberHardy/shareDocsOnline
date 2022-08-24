from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
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


def delete_file(request, pk):
    try:
        deleted_file = get_object_or_404(Document, pk=pk)
        deleted_file.delete()
    except Document.DoesNotExist:
        raise Http404("Given query not found....")

    return redirect('choose_file')
