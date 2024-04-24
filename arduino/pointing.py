class NAO:
    def __init__(self):
        pass
    
    def verbinden(self, ip, port):
        # Implementeer de logica om verbinding te maken met de robot op het opgegeven ip en poort
        pass
    
    def watKanIk(self):
        # Implementeer de logica om de mogelijkheden van de robot op te halen
        return "Mogelijkheden van de robot"
    
    def allesWatJeWil(self, beweging):
        # Implementeer de logica om de opgegeven beweging uit te voeren
        print("Ik voer de beweging uit: {beweging}")


def main():
    nao = NAO()
    nao.verbinden("169.254.56.184", 9559)  
    print(nao.watKanIk())
    print()
    movement = input("Wat wil je dat ik doe: ")
    nao.allesWatJeWil(movement)


if __name__ == "__main__":
    main()

