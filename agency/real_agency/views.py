from django.shortcuts import render

def index(request):
    context = {
        'title': 'Real Estate Agency',
    }
    return render(request, 'real_agency/index.html', context=context)
