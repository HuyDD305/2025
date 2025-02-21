# usf = input("Enter the US Floor Number: ")
# wf = int(usf) - 1
# print('Non-US Floor Number is', wf)

class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


if __name__ == "__main__":
    an = PartyAnimal()
    an.party()
    an.party()
    an.party()