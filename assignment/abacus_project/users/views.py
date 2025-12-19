
# Create your views here.

from django.shortcuts import render, redirect
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = UserProfile.objects.get(
                username=username,
                password=password
            )
            request.session["user_id"] = user.id
            return redirect("profile")
        except UserProfile.DoesNotExist:
            return render(request, "login.html", {
                "error": "Invalid credentials"
            })

    return render(request, "login.html")


def profile_view(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("login")

    user = UserProfile.objects.get(id=user_id)
    return render(request, "profile.html", {"user": user})


def about_view(request):
    return render(request, "about.html")
