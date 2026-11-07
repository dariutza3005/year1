
def display_ladder(steps):
    for i in range(steps):
        print("|  |")
        print("****")

def create_ladder():
    steps = int(input("Enter the number of steps: "))
    display_ladder(steps)

create_ladder()
