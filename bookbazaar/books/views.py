from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required


def home(request):
    books = Book.objects.filter(is_sold=False).order_by("-date_posted")
    return render(request, "books/home.html", {"books": books})


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})
