import random

PREFIXES = [
    "ka", "ke", "ki", "ko", "ku",
    "ra", "re", "ri", "ro", "ru",
    "la", "le", "li", "lo", "lu",
    "na", "ne", "ni", "no",
    "va", "ve", "vi", "vo",
    "za", "ze", "zi",
    "xa", "xe"
]

MIDDLES = [
    "v", "x", "z", "r", "l", "n",
    "m", "t", "k", "d", "b", "f"
]

SUFFIXES = [
    "io",
    "ix",
    "on",
    "ex",
    "ox",
    "ium",
    "ora",
    "era",
    "ium",
    "ify",
    "labs",
    "core",
    "base",
    "flow",
    "link",
    "grid",
    "nova",
    "byte",
    "forge"
]

VOWELS = "aeiou"


def readable(name: str) -> bool:
    count = 0
    last = None

    for c in name.lower():
        current = c in VOWELS

        if current == last:
            count += 1
        else:
            count = 1

        last = current

        if count >= 3:
            return False

    return True


def generate_name():
    while True:

        mode = random.randint(1, 3)

        if mode == 1:
            name = random.choice(PREFIXES) + random.choice(SUFFIXES)

        elif mode == 2:
            name = (
                random.choice(PREFIXES)
                + random.choice(MIDDLES)
                + random.choice(SUFFIXES)
            )

        else:
            name = (
                random.choice(PREFIXES)
                + random.choice(MIDDLES)
                + random.choice(MIDDLES)
                + random.choice(SUFFIXES)
            )

        if 5 <= len(name) <= 9 and readable(name):
            return name.capitalize()


def generate_names(count=100):

    names = set()

    while len(names) < count:
        names.add(generate_name())

    return sorted(names)
