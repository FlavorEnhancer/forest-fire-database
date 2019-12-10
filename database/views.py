from django.shortcuts import render


def directions(request):
    return render(request, 'database_directions.html')
