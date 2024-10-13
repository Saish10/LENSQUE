from datetime import datetime
from django.shortcuts import render
from .models import Photo, Category


def home(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    current_year = datetime.now().year
    return render(
        request,
        "home.html",
        {"categories": categories, "photos": photos, "year": current_year},
    )


def category_photos(request, category_id):
    photos = Photo.objects.filter(category_id=category_id)
    return render(request, "category_photos.html", {"photos": photos})
