from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def views(request):
    return render(request, 'files/index.html')
    # return HttpResponse("Hello world. You're it puddle index.")
