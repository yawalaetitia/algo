note=[12,13,15,17]
persone={"nom":"ouattara", "prenom":"yawa", "village":"kopingué", "age":24}
print("Bonjour Miss", persone["nom"], persone["prenom"],". Vous venez de ",persone["village"], "et vous avez", persone["age"])
print("Bonjour Miss "+persone["nom"]+" "+persone["prenom"]+". Vous venez de "+persone["village"]+" et vous avez "+str(persone["age"]))
print(f"Bonjour Miss {persone['nom']} {persone['prenom']}. Vous venez de {persone['village']} et vous avez {persone['age']} ans.")
print("Bonjour Miss {} {}. Vous venez de {} et vous avez {} ans.".format(persone["nom"],persone["prenom"],persone["village"],persone["age"])) 