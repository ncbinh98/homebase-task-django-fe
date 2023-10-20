from django.shortcuts import render
import requests

def get_users_from_api():
    proxy_url = 'http://localhost:5000/users' 
    try:
        response = requests.get(proxy_url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
# Create your views here.
def user_list(request):
    users = get_users_from_api()
    # return JsonResponse(users, safe=False)
    return render(request, 'users/user_list.html', {'users': users})
