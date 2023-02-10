import requests


def main():
    """

    :return:
    """
    URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
    KEY = 'ZmRjYzE2NzctODA3My00OWZhLWI3MzgtYTk0Njk0NjE2OTYwOjE1ZTYzMmQxNGE1NjQ0NDM5ZDg5NjYyNGI3OTMyYjU5'

    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)
    if auth.status_code == 200:

        while True:
            word = input("Введите слово для перевода: ")
            if word:
                headers_translate = {'Authorization': 'Bearer ' + auth.text}
                params = {'text': word, 'srcLang': 1033, 'dstLang': 1049}
                rec = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
                r = rec.json()
                try:
                    print(r['Translation']['Translation'])
                except:
                    print("Мы не знаем такого слова")
    else:
        print("Error!")

if __name__ == '__main__':
    main()


