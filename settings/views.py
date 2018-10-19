from django.shortcuts import render


def vue(request):
    options = '{}'
    if not request.user.is_authenticated():
        return render(request, 'index.html', locals())

    user = request.user
    '''
    load user info here
    '''

    return render(request, 'index.html', locals())
