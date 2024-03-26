from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required


def add_book(request):
    template_name = 'book/add.html'
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def show_books(request):
    template_name = 'book/show.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template_name, context)


def update_book(request, pk):
    template_name = 'book/add.html'
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)



def delete_book(request, pk):
    obj = Book.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'book/confirm.html')
