import requests

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809'
}

response = requests.get('https://cnys.tv/vodplay-2250-1-9.html', proxies=proxies)
print(response.text)