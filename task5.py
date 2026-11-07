
def display_ladder(steps):
    for i in range(steps):
        print("|-----|")

def create_ladder():
    steps = int(input("How many steps? "))
    display_ladder(steps)

create_ladder()
