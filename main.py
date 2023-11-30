import pronotepy
import datetime
from pronotepy.ent import ent_hdf

client = pronotepy.Client("https://0620052v.index-education.net/pronote/eleve.html", # lien du pronote du lycée
                          username="", # nom d'utilisateur ENT
                          password="", # mot de passe ENT
                          ent=ent_hdf) # ça marche avec les cookies qu'il récupére


def main():
    if client.logged_in:
        print(f'Client connecté ! Username: {client.username} | Password: {client.password}')

        periods = client.periods # Notes

        for period in periods:
            for grade in period.grades:
                print(f'Note de {grade.subject.name} : {grade.grade}/{grade.out_of}')

        # Devoirs
        homework = client.homework(datetime.date.today())
        for home in homework:
            print(f'{home.subject.name} : {home.description}')

    else:
        print("Connexion au Client échoué !")


if __name__ == '__main__':
    main()