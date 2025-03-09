import pronotepy
import datetime

# if you're using Pronote with an ENT then you have to import it
from pronotepy.ent import ent_hdf

client = pronotepy.Client("https://0620052v.index-education.net/pronote/eleve.html", # link of the pronote of your establishment
                          username="", # ENT username
                          password="", # ENT password
                          ent=ent_hdf) # by passing the ENT, the dependency will look at your cookies of your web browser


def main():
    if client.logged_in:
        print(f'Client connected ! Username: {client.username} | Password: {client.password}')

        periods = client.periods

        for period in periods:
            # Grades
            for grade in period.grades:
                print(f'Name of the Grade {grade.subject.name} : {grade.grade}/{grade.out_of}')

        # Homeworks
        homework = client.homework(datetime.date.today())
        for home in homework:
            print(f'{home.subject.name} : {home.description}')

    else:
        print("Connection to the Client failed !")


if __name__ == '__main__':
    main()