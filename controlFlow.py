def redirectionUrl(language: str) -> str:
    domain = 'www.example.org/'
    if language == 'English':
        return domain + 'en'
    elif language == 'Japanese':
        return domain + 'ja'
    elif language == 'Spanish':
        return domain + 'es'
    elif language == 'Russian':
        return domain + 'ru'
    else:
        domain
