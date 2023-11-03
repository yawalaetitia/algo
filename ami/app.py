from pyami_asterisk import AMIClient

# on se connecte à asterisk ami
try:
    ami = AMIClient(
        host="192.168.50.66", port=5038, username="tester", secret="the_tester"
    )
except Exception as e:
    print(e)

# afficher l'évènement de originate    
def callback_originate(events):
    print(events)

# afficher l'évènement de hangup et fermer la connexion 
async def Hangup_callback(events):
    if events.get("Event") == "Hangup":
        print(events)
        await ami.connection_close()
        
# CREATION DE DEUX TABLEAU POUR STOCKER LES DONNÉES
# correspond aux differents lieux de destination
lieux_destination = [
    "Abidjan",
    "Abengourou",
    "Aboisso",
    "Bondougou",
    "Bouna",
    "Bouake",
    "Boundiali",
    "Daloa",
    "Divo",
    "Ferkessedougou",
    "Gagnoa",
    "Katiola",
    "Kong",
    "Lakota",
    "Odienne",
]

# correspond aux differents départs
liste_depart = {
    "1": "5 heure 00 minute",
    "2": "6 heure 00 minute",
    "3": "7 heure 00 minute",
}

# DEBUT DU PROGRAMME
print("\033[33m---------------------- ~~ ----------------------")
print("BIENVENUE SUR LE FORMULAIRE DE RESERVATION DE TICKET")
print("VEUILLEZ RENSEIGNER TOUS LES CHAMPS POUR EFFECTUER LA RESERVATION")
print("\n")

print("~~ ----  INFORMATIONS PERSONNELLES ---- ~~")
print("\033[32m* ENTREZ VOTRE NOM ET PRENOMS")
fullname = input("\033[34m>> ").strip().upper()
if fullname == "":
    print("\033[31mErreur!")
    exit(0)
print("\n")

print("\033[32m* QUELLE EST VOTRE GENRE : SAISIR F POUR FEMME ET H POUR HOMME")
genre = input("\033[34m>> ").strip().upper()
titre=""
if genre != "F" and genre != "H":
    print("\033[31mErreur!")
    exit(0)

if genre == "F":
    titre="Madame"
if genre == "H":
    titre="Monsieur"
print("\n")

print("\033[32m* ENTREZ VOTRE CONTACT")
contact = input("\033[34m>> ").strip().upper()
if not contact.isdigit() :
    print("\033[31mErreur!")
    exit(0)
print("\n")

print("\033[32m* ENTREZ VOTRE LIEUX D'HABITATION")
localisation = input("\033[34m>> ").strip().upper()
if localisation == "":
    print("\033[31mErreur!")
    exit(0)
print("\n")

print("\033[33m~~ ----  DETAILS DE LA RESERVATION ---- ~~")
print("-- LISTE DES VILLES DE DESTINATION --")
for dest in lieux_destination:
    print(f"\033[33m{dest.upper()}")
print("\033[32m* ENTREZ VOTRE DESTINATION PARMIS CELLES DANS LA LISTE CI-DESSUS.")
destination = input("\033[34m>> ").strip().upper()
if destination.capitalize() not in lieux_destination :
    print("\033[31mErreur!")
    exit(0)
print("\n")

print("\033[32m* COMBIEN DE TICKET VOULEZ RESERVER ? (ENTRE 1 ET 5)")
ticket=input("\033[34m>> ").strip().upper()
if int(ticket) not in range(1,6):
    print("\033[31mErreur!")
    exit(0)
print("\n")

print("\033[33m-- LISTE DES DEPARTS --")
for dep in liste_depart:
    print(f"DEPART : {dep} - {liste_depart[dep]}")
print("\033[32m* QUELLE DEPART VOULEZ VOUS PRENDRE ? (ENTREZ LE NUMERO DU DEPART VOULU)")
depart = input("\033[34m>> ").strip().upper()
if int(depart) not in range(1,4):
    print("\033[31mErreur!")
    exit(0)

# afficher les informations remplies
print("\n")
print("\033[33m------------------------------------")
print("~~ --- RECU --- ~~")
print("\033[34mNOM ET PRENOMS :","\033[32m",fullname)
print("\033[34mGENRE :","\033[32m",genre)
print("\033[34mCONTACT :","\033[32m",contact)
print("\033[34mLOCALISATION :","\033[32m",localisation)
print("\033[34mDESTINATION :","\033[32m",destination)
print("\033[34mNOMBRE DE TICKET :","\033[32m",ticket)
print("\033[34mNUMERO DU DEPART :","\033[32m",f"{depart} : {liste_depart[depart]}")
print("\033[32mCONFIRMEZ LES INFORMATIONS ? `O` pour Oui ou `N` pour Non")

# on demande confirmation des informations
confirm = input(">> ").upper()
while confirm!= 'O' and confirm!='N':
    confirm = input(">> ").upper()

# s'il refuse on arrête tout
if confirm == 'N':
    print("\033[31mRESERVATION ANNULEE!")
    print("\033[33m~~ - BYE! - ~~~")
    exit(0)
else:
    # sinon on l'appel
    ami.create_action(
        {
            "Action": "Originate",
            "Exten": "400",
            "Channel": "SIP/6003",
            "Context": "work",
            "Priority": "1",
            "Variable": f"TITRE={titre},NOM={fullname},DESTINATION={destination},DEPART={liste_depart[depart]}",
            "Async": "true",
        },
        callback_originate,
    )
    ami.register_event(["Originate"], callback_originate)
    ami.register_event(["Hangup"], Hangup_callback)
    ami.connect()