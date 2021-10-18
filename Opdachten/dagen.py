dagen = input("Welke dagen? ")
dag = ""

while dagen != dag:
    if dag == "Maandag":
        dag = "Dinsdag"
    elif dag == "Dinsdag":
        dag = "Woensdag"
    elif dag == "Woensdag":
        dag = "Donderdag"
    elif dag == "Donderdag":
        dag = "Vrijdag"
    elif dag == "Vrijdag":
        dag = "Zaterdag"
    elif dag == "Zaterdag":
        dag = "Zondag"
    elif dag == "Zondag":
        dag = "Einde van de week"
    else:
        dag = "Maandag"
    print(dag)
    