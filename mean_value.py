# Medelvärde

def main():
    text = input("")
    str_nummer = text.split(',')
    nummer_lista = []
    for nummer in str_nummer:
        nummer_lista.append(int(nummer))

    print(sum(nummer_lista) / len(nummer_lista))

if __name__ == "__main__":
    main()
