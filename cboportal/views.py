from django.shortcuts import render

def index(request):
    """the root url path for the reporting app

    Parameters
    ----------
    request: django.request
        the request object provided by the framework

    Returns
    -------
    HttpResponse
        render of the reporting.index.html template
    """

    return render(request, 'application.html')
