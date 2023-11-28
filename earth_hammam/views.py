from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'errors.html', {
            'text': "We are sorry, but we could not find the page you are looking for."  # noqa
        })

def error_500(request, *args, **argv):
    return render(request, 'errors.html', {
            'text': "We are sorry, this should not happen but we just encountered an error."   # noqa
        })

def error_403(request, exception):
    return render(request, 'errors.html', {
            'text': "You shall not enter! I have spoken."
        })

def error_400(request, exception):
    return render(request, 'errors.html', {
            'text': "This did not work. There seems to be a communication error."   # noqa
        })
