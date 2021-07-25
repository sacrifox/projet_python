#importation des modules nécessaires
import ftplib, os

#fonction de connexion
def connexion_ftp(host, user, password):
    while True:
        try:
            ftp = ftplib.FTP(host, user, password)
            print(ftp.getwelcome())  # message de bienvenue
            print("Répertoire courant", ftp.pwd())  # affiche le répertoire courant"
            ftp.dir()  # listing du répertoire courant
            commande_ftp(ftp)
            break
        except ftplib.all_errors as e:
            print("Connexion échoué, vérifié vos identifiants.", e)


#fonction commandes avec toutes les possibilités
def commande_ftp(ftp):
    while True:
        command = input("Entrez une commande : ")
        commands = command.split()  # Permet de fractionner une chaîne en liste ou chaque mot est un élément de liste

        if commands[0] == 'cd':  # Changer de répertoir
            try:
                ftp.cwd(commands[1])
                print("Répertoire de", ftp.pwd())
                ftp.dir()
                print("Répertoire actuel", ftp.pwd())
                if commands[1] == None:
                    print("erreur, veuillez ressaisir")
                    continue
            except ftplib.error_perm as e:  # erreur 550. Permissions incorrectes
                error_code = str(e).split(None, 1)
                if error_code[0] == "550":
                    print(error_code[1], "Le répertoire n'existe ou vous n'avez pas les permissions pour regarder.")


        elif commands[0] == "get":  # téléchargement d'un fichier
            try:
                nom_local=input("si vous le souhaitez, entrez un nom personnalisé pour votre fichier : ")
                if nom_local==None:
                    nom_local=commands[1]
                with open(os.path.join("d:", nom_local), "wb") as f:
                    ftp.retrbinary("RETR" + commands[1], f.write)
                    print("Fichier téléchargé avec succès")
            except ftplib.error_perm as e:  #erreur 550. Permissions incorrectes
                error_code = str(e).split(None, 1)
                if error_code[0] == "550":
                    print(error_code[1], "Le répertoire n'existe ou vous n'avez pas les permissions pour regarder.")


        elif commands[0] == "push": #téléversement d'un fichier
            chemin_local = input("Renseignez le chemin de votre fichier :")
            fichier_local = input("Renseignez le nom de votre fichier : ")
            chemin_local, fichier_local = os.path.split (nom_split)
            with open(nom_split, "rb") as f:
                ftp.storbinary("STOR" + fichier_local, f)



        elif commands[0] == "ls":  # Liste les répertoires
            print('Directory of', ftp.pwd())
            ftp.dir()


        elif commands[0] == "size": #Taille d'un fichier
            ftp.sendcmd("TYPE I") #passage en mode binaire
            taille_ftp = ftp.size(commands[1]) #donne la taille en octets
            if taille_ftp != None:
                print (taille_ftp, "octets")
            else:
                print ("méthode 'ftp.size()' insupporté par le serveur ftp")


        elif commands[0] == "exit":  # Sortir de l'application
            try:
                ftp.quit()  # méthode de fermeture propre avec interaction serveur
                break
            except:
                ftp.close()  # méthode sec, rupture côté client






a=input("entrez le nom de l'hôte : ")
b=input("entrez le nom de l'utilisateur : ")
c=input("entrez le mot de passe : ")
connexion_ftp(a,b,c)

#document = r"C:\Users\Loïc\Documents\Planification de projet.pdf" #fichier d'exemple dédiée à l'envoie sur le serveur



##gestion des logs 

