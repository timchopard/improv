from django.shortcuts import render

def bern_index(request):
    return render(request, "bern/index.html")