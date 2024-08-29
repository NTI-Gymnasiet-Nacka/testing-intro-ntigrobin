# Största skillnad

def main():
    text = input("")
    str_nummer = text.split(',')
    nummer_lista = []
    for nummer in str_nummer:
        nummer_lista.append(int(nummer))

    max_nummer = max(nummer_lista)
    min_nummer = min(nummer_lista)

    print(max_nummer - min_nummer)

if __name__ == "__main__":
    main()
