import requests
from config import GITHUB_API, HEADERS


def is_available(name: str) -> bool:
    """
    GitHub kullanıcı veya organizasyon adının uygun olup olmadığını kontrol eder.
    True  = Kullanılabilir
    False = Kullanımda
    """

    url = f"{GITHUB_API}/users/{name.lower()}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 404:
            return True

        if response.status_code == 200:
            return False

        return False

    except requests.RequestException:
        return False
