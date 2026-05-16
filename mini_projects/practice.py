def main():
    passwort()

def passwort():
    while True:

        eingabe = input("Bitte Passwort eingeben: ")
        
        if eingabe == "python123":
            print("Zugriff erlaubt")
            break

        else:
            print("Falsches Passwort")

main()