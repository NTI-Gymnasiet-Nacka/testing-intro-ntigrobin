# Vokalräkning

def main():
    text = input("")
    
    vokaler = "aeiouyåäöAEIOUYÅÄÖ"
    antal_vok = 0

    for u in text:
        if u in vokaler:
            antal_vok += 1

    print(antal_vok)

if __name__ == "__main__":
    main()
