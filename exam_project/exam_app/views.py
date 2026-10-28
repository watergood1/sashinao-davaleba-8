from django.shortcuts import render

def films(request):
    lst = ["avatar", "titanic", "inception"]

    context = {
        "avatar":7
        "titanic":8
        "inception":10
    }

    return render(request, "films.html", context)

# Create your views here.
