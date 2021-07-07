from celery import shared_task
from time import sleep, time

from django.contrib.auth.models import User
from requests import get

from manager.models import AccountUser


@shared_task
def first_task():

	return 'first task is done'

@shared_task
def second_task():
	return 'second_task is done'

@shared_task
def check_users():
	git_hub_users = AccountUser.objects.all()
	for user in git_hub_users:
		url = f'https://api.github.com/users/{user.github_account}/repos'
		response = get(url)
		repos = [i['name'] for i in response.json()]
		user.github_repos = repos
		user.save()


# def users_repos():
# 	users_list = User.objects.all()
# 	 for user in users_list:
#
# 		code = request.GET.get('code')
# 		url = f'https://github.com/login/oauth/access_token?client_id={GIT_CLIENT_ID}&client_secret={GIT_CLIENT_SECRET}' \
# 			  f'&code={code}'
# 		response = post(url, headers={'Accept': 'application/json'})
# 		token = response.json()['access_token']
# 		url = 'https://api.github.com/user'
# 		response = get(url, headers={"Authorization": f'token {token}', 'Accept': 'application/json'})
# 		user_name = response.json()['login']
# 		url = f'https://api.github.com/users/{user_name}/repos'
# 		response = get(url, headers={"Authorization": f'token {token}', 'Accept': 'application/json'})
# 		data = [i['name'] for i in response.json()]


