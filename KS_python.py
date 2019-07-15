def token():
    from urllib.parse import urlencode
    APP_ID = 7056106
    AUTH_URL = 'https://oauth.vk.com/authorize'
    AUTH_DATA = {'client_id': APP_ID, 'display': 'page', 'scope': 'friends', 'response_type': 'token'}
    print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))

def mutual_friend():
    import requests
    TOKEN = '0872e09e7652d24bcdb9ec71b53c2b78ec1b35deb0777fb95294c6cce42be7a80da85a2ba1d2401e8c489'
    params = {
        'access_token': TOKEN,
        'order': 'hints',
        'v': '5.52'
    }

    friends_get_params = params.copy()
    friends_get_params['user_id'] = input('Введите id user № 1: ')
    response = requests.get('https://api.vk.com/method/users.get', params=friends_get_params)
    print('User № 1: ', response.json()['response'])
    response = requests.get('https://api.vk.com/method/friends.get', params=friends_get_params)
    user_1 = response.json()['response']['items']

    friends_get_params = params.copy()
    friends_get_params['user_id'] = input('Введите id user № 2: ')
    response = requests.get('https://api.vk.com/method/users.get', params=friends_get_params)
    print('User № 2: ', response.json()['response'])
    response = requests.get('https://api.vk.com/method/friends.get', params=friends_get_params)
    user_2 = response.json()['response']['items']

    mutual_friend = set(user_1) & set(user_2)
    print('Общие друзья: ')
    for i in mutual_friend:
        friends_get_params['user_id'] = i
        response = requests.get('https://api.vk.com/method/users.get', params=friends_get_params)
        print(response.json()['response'])

def command():
    command = input('Внимание! Для работы кода необходим TOKEN.\nЕсли вы внесли TOKEN в код нажмите "y",\nиначе нажмите "n",\nполучте TOKEN,\nвнесите его в код \nи, заново запустив программу, нажмите "y"\nВаша команда: ')
    if command == 'n':
        token()
    elif command == 'y':
        mutual_friend()
    else:
        print('Ошибка ввода. Введенной вами команды не существует. Запустите программу заново.')

if __name__ == "__main__":
    command()