from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'errors.html', {
            'text': "404 - We are sorry, but we could not find the page you are looking for."  # noqa
        })

def error_500(request, *args, **argv):
    return render(request, 'errors.html', {
            'text': "500 - We are sorry, this should not happen but we just encountered an error."   # noqa
        })

def error_403(request, exception):
    return render(request, 'errors.html', {
            'text': "403 - Access forbidden."
        })

def error_400(request, exception):
    return render(request, 'errors.html', {
            'text': "400 - This did not work. There seems to be a communication error."   # noqa
        })
