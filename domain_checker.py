import socket


def is_domain_available(domain: str) -> bool:
    """
    Basit DNS kontrolü.
    True  = Muhtemelen kullanılabilir
    False = DNS kaydı var
    """

    try:
        socket.gethostbyname(domain)
        return False
    except socket.gaierror:
        return True


def check_domains(name: str):

    extensions = [
        ".com",
        ".ai",
        ".io",
        ".dev"
    ]

    results = {}

    for ext in extensions:
        domain = name.lower() + ext
        results[domain] = is_domain_available(domain)

    return results
