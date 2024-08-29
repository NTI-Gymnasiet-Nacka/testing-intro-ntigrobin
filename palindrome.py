# Palindrome

def main():
    text = input("")
    text_lista = []
    for u in text:
        text_lista.append(u)
    if text[::-1] == text:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
