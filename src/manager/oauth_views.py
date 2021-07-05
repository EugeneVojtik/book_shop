from django.contrib.auth import login
from django.shortcuts import render
from requests import post, get

from book_shop.settings import GIT_CLIENT_ID, GIT_CLIENT_SECRET


def brazzers_view(request):
    url = f'https://github.com/login/oauth/authorize?client_id={GIT_CLIENT_ID}'
    return render(request, 'brazzers.html', {'url': url})


def brazzers_callback_view(request):

    code = request.GET.get('code')
    url = f'https://github.com/login/oauth/access_token?client_id={GIT_CLIENT_ID}&client_secret={GIT_CLIENT_SECRET}' \
          f'&code={code}'
    response = post(url, headers={'Accept': 'application/json'})
    token = response.json()['access_token']
    url = 'https://api.github.com/user'
    response = get(url, headers={"Authorization": f'token {token}', 'Accept': 'application/json'})
    user_name = response.json()['login']
    url = f'https://api.github.com/users/{user_name}/repos'
    response = get(url, headers={"Authorization": f'token {token}', 'Accept': 'application/json'})
    data = [i['name'] for i in response.json()]

    return render(request, 'brazzers.html', {'data': data})


