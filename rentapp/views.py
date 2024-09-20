from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')
def homepage(request):
    print("Rendering homepage...")
    return render(request, 'homepage.html')
