from threading import Thread


class Connexion(Thread):

    login = "serge"
    password = "delacompta"

    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Connexion.__instance is None:
            Connexion()
        return Connexion.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Connexion.__instance is not None:
            print("This class is a singleton!")
        else:
            Connexion.__instance = self
            Thread.__init__(self)

    def run(self):
        # alumer la LED verte
        print("Try to connect with login ", Connexion.login, " and password ", Connexion.password)
        # faire clignoter la LED verte
