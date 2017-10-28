from mohameda_csc236L2 import*
def main():
    """The map class. It opens the map file and reads it and finding the treasure in it by going in 4 different directions"""
    print("Welcome to the cave! Buckle up!!")
    try:
        file1 = int(input("Which map to choose? Enter 1 for map one, 2 for map two and 3 for map three:"))
        if file1==1:
            file1="sample_input_map_one.txt"
        elif file1==2:
            file1= "sample_input_map_two.txt"
        else:
            file1= "sample_input_map_three.txt"
    except:
        print("Enter a number please")
    game = Map() # map class object
    game.make_map(file1)
    game.finding_m()
    game.check_m()
    game.decide_next_step()
    game.next_step()
main() # A call to main
