from django.shortcuts import render


def database_directions(request):
    return render(request, 'database_directions.html')
