from django.shortcuts import render

def handler404(request, exception):
    """ Handle 404 errorsm """
    return render(request, 'errors/404.html', status=404)