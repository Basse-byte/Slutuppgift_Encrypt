# Skapa ett verktyg som kan:
# Generera och spara en krypteringsnyckel.
# Kryptera en given fil med hjälp av en symmetrisk nyckel.
# Dekryptera en krypterad fil med rätt nyckel.
# Använd cryptography-biblioteket (Fernet rekommenderas)
# Använd argparse-biblioteket för att ta argument

# Krav:
# Implementera ett skript som använder argparse för att hantera
# kommandoradsalternativ och utför följande funktioner:
# Generera en symmetrisk nyckel och spara den i en fil.
# Kryptera en fil med en befintlig nyckel.
# Dekryptera en krypterad fil och återställa originalet.

# Förslag på extrafunktioner (frivilligt):
# Implementera felhantering för fil som saknas
# Lägg till funktionalitet för att skapa en lösenordsbaserad nyckel med
# hjälp av PBKDF2.

from cryptography.fernet import Fernet
import os
import argparse
import pyfiglet

ascii_art = pyfiglet.figlet_format("Encrypt / Decrypt")
print(ascii_art)

key = None # Skapar variabeln key utan något värde för att senare tilldela.

## Genererar krypteringsnyckeln och sparar i en fil: #######################################################################
def key_generation():
    global key # Säger att key är en global variabel för att den ska kunna användas i flera funtioner.

    key = Fernet.generate_key() # Genererar en nyckel i binär data
    print(f"Nyckel genererad: {key.decode()}") # key.decode() formaterar om nyckeln till vanliga tecken.

    with open("ENC_key.key", "wb") as file: # filnamn.key för att filen ska bli en binär nyckel. "wb" skapar i binärt format.
        file.write(key) # Skriver in key i filen.

    print(f"Nyckel sparad i filen ENC_key")

## Läser in den tidigare genererade nyckeln i programmet ##################################################################
def load_key():
    global key

    with open("ENC_key.key", "rb") as file: # Öppnar filen med nyckeln som genererats i tidigare funktion ##################
        key = file.read() # variabeln key blir innehållet i filen. Vilket är krypteringsnyckeln.

    print(f"Nyckeln har lästs in")

## Krypterar fil med nyckeln ###############################################################################################
def encrypt_file(filename): # filename är det som användaren matar in. Filnamn i nuvarande mapp eller filsökväg.
    global key
    cipher_suite = Fernet(key) # Variabeln cipher_suite får värdet från Fernet key objektet.

    if not os.path.exists(filename):
        print(f"Filen {filename} du vill kryptera verkar inte finnas")
        return

    with open(filename, "rb") as file: # Läser in filen binärt
        secret_file = file.read()

    cipher_file = cipher_suite.encrypt(secret_file) # Variabeln cipher_file innehåller nu den krypterade versionen av secret_file.

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(cipher_file) # cipher_file sparas istället för originalfilen.
    
    print(f"Filen {filename} har krypterats och sparats")


## Dekrypterar fil med nyckeln ############################################################################################
def decrypt_file(filename):
    global key
    cipher_suite = Fernet(key) # Variabeln cipher_suite får värdet från Fernet key objektet. Igen eftersom detta sker i enskilda funktioner och den förra är inte längre in scope.

    if not os.path.exists(filename): # Felhantering med hjälp av os path. Om användarinmatningen inte finns, kommer meddelande:
        print(f"Filen {filename} du vill kryptera verkar inte finnas")
        return

    with open(filename, "rb") as file: # Läser filen i binär data.
        enc_file = file.read()

    decrypted_file = cipher_suite.decrypt(enc_file) # Variablen decrypted_file får innehållet från enc_file som nu är dekrypterat

    with open(filename, "wb") as file: 
        file.write(decrypted_file) # Filen sparas som okrypterad

    print(f"Filen {filename} har dekrypterats och kommer nu att öppnas")

    os.startfile(filename) # en dekrypterade filen körs, because why not? Det är Rick-tigt kul >:)

if __name__ == "__main__": # Bara för att det måste vara så?! och för att kontrollera om programmet körs som fristående program eller importeras som modul i ett annat program.
    parser = argparse.ArgumentParser(description="Med detta script kan du göra följande: Generera krypteringsnyckel, kryptera och dekryptera valfri fil.")
    parser.add_argument("action", choices=["generate_key", "encrypt", "decrypt"], help="Vad vill du göra?")
    parser.add_argument("filename", nargs="?", help="Ska denna fil krypteras eller dekrypteras?")
    args = parser.parse_args() # Läser in användarens val i action och filename.

    if args.action == "generate_key": 
        key_generation() # Om input är generate_key körs funktionen som genererar nyckeln.
    elif args.action == "encrypt": # Om input är encrypt:
        if args.filename: # och om input har filnamn/filsökväg som finns körs 2 funktionerna:
            load_key()
            encrypt_file(args.filename)
        else: # Annars säger den att du har gjort FEL :(
            print(f"Du måste ange vilken fil i denna mapp eller fullständig filsökväg till annan fil som du vill kryptera")
    elif args.action == "decrypt": # Om input är decrypt, och.....
        if args.filename: # om input innehåller filnamn/filsökväg körs 2 funktioner:
            load_key()
            decrypt_file(args.filename)
        else: # Om du inte anger filnamn/sökväg, F-you :)
            print(f"Du måste ange vilken fil i denna mapp eller fullständig filsökväg till annan fil som du vill dekryptera")

## SLUT! #############################################################################################################################
######################################################################################################################################

# Eller ska man implementera pyfiglet som presentation i programmet? c: