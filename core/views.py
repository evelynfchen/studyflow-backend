from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category
from django.db.models.functions import Lower


@login_required
def home(request):
    return render(request, "home.html")

def validate_category_name(request, user, category=None):
    """Validate category name for create/update and prevent duplicates per user."""
    name = (request.POST.get("name") or "").strip()

    if not name:
        return None, "Name is required."

    query = Category.objects.filter(user=user, name=name)
    if category is not None:
        query = query.exclude(pk=category.pk)

    if query.exists():
        return None, "Category already exists."

    return name, None

@login_required
def category_list(request):
    sort = request.GET.get("sort", "name_asc")

    categories = Category.objects.filter(user=request.user)

    if sort == "name_desc":
        categories = categories.order_by(Lower("name").desc())
    else:
        categories = categories.order_by(Lower("name").asc())

    context = {
        "categories": categories,
        "sort": sort,
    }
    return render(request, "feature1/category_list.html", context)


@login_required
def category_create(request):
    if request.method == "POST":
        name, error = validate_category_name(request, request.user)

        if error:
            return render(request, "feature1/category_form.html", {"error": error})

        Category.objects.create(user=request.user, name=name)
        return redirect("category_list")

    return render(request, "feature1/category_form.html")


@login_required
def category_update(request, pk: int):
    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == "POST":
        name, error = validate_category_name(request, request.user, category=category)

        if error:
            return render(
                request,
                "feature1/category_form.html",
                {"category": category, "error": error},
            )

        category.name = name
        category.save()
        return redirect("category_list")

    return render(request, "feature1/category_form.html", {"category": category})


@login_required
def category_delete(request, pk: int):
    category = get_object_or_404(Category, pk=pk, user=request.user)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(request, "feature1/category_confirm_delete.html", {"category": category})
