import random

START = [
    "ka", "ke", "ki", "ko", "ku",
    "ra", "re", "ri", "ro", "ru",
    "va", "ve", "vi", "vo",
    "ze", "zi", "za",
    "lo", "lu", "le",
    "no", "ne", "ni",
    "xa", "xe", "xo"
]

END = [
    "ra", "ro", "rix", "va", "vo",
    "tek", "zen", "nova", "labs",
    "ly", "fy", "bit", "io",
    "go", "max", "core", "soft",
    "hub", "link", "base"
]


def generate_name():
    while True:
        name = random.choice(START) + random.choice(END)
        if 5 <= len(name) <= 10:
            return name.capitalize()


def generate_names(count=100):
    names = set()

    while len(names) < count:
        names.add(generate_name())

    return sorted(names)
