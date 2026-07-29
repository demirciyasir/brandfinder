from generator import generate_names
from github_checker import is_available


def main():
    print("BrandFinder v1.0\n")

    names = generate_names(100)

    available = []

    for name in names:
        if is_available(name):
            print(f"✅ {name}")
            available.append(name)
        else:
            print(f"❌ {name}")

    with open("available_names.txt", "w", encoding="utf-8") as f:
        for name in available:
            f.write(name + "\n")

    print(f"\nToplam {len(available)} uygun isim bulundu.")
    print("Sonuçlar: available_names.txt")


if __name__ == "__main__":
    main()
