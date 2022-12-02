# KÓŁKO I KRZYŻYK

def board():
    print("      |       |      ")
    print("   " + one + "  |   " + two + "   |  " + three + "  ")
    print("______|_______|______")
    print("      |       |      ")
    print("   " + four + "  |   " + five + "   |  " + six + "  ")
    print("______|_______|______")
    print("      |       |      ")
    print("   " + seven + "  |   " + eight + "   |  " + nine + "  ")
    print("      |       |      ")    

win = False
counter = 0
one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "
counter = 0
ways = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
positions = [one, two, three, four, five, six, seven, eight, nine]
lst = []

print('INSTRUKCJA - numery pol')
print("      |       |      ")
print("   " + "1" + "  |   " + "2" + "   |  " + "3" + "  ")
print("______|_______|______")
print("      |       |      ")
print("   " + "4" + "  |   " + "5" + "   |  " + "6" + "  ")
print("______|_______|______")
print("      |       |      ")
print("   " + "7" + "  |   " + "8" + "   |  " + "9" + "  ")
print("      |       |      ")    
print("\n\n")

while win == False:
    ways = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
    board()

    print("First player's move:")
    placement = int(input())
    if placement == 1:
        one = "o"
    elif placement == 2:
        two = "o"
    elif placement == 3:
        three = "o"
    elif placement == 4:
        four = "o"
    elif placement == 5:
        five = "o"
    elif placement == 6:
        six = "o"
    elif placement == 7:
        seven = "o"
    elif placement == 8:
        eight = "o"
    elif placement == 9:
        nine = "o"
    else:
        print("invalid entry")
        break

    ways = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
    for element in ways:
        if all(position == "o" for position in element):
            win = True
            board()
            print('WINNER WINNER - "O"')
            break
        else:
            None

    if win == True:
        break

    positions = [one, two, three, four, five, six, seven, eight, nine]
    counter = 0
    for position in positions:
        if position != ' ':
            counter += 1
    if counter == 9:
        board()
        print("UNLUCKY - TIE")
        break


    board()
    print("Second player's move:")
    placement = int(input())
    if placement == 1:
        one = "x"
    elif placement == 2:
        two = "x"
    elif placement == 3:
        three = "x"
    elif placement == 4:
        four = "x"
    elif placement == 5:
        five = "x"
    elif placement == 6:
        six = "x"
    elif placement == 7:
        seven = "x"
    elif placement == 8:
        eight = "x"
    elif placement == 9:
        nine = "x"
    else:
        print("invalid entry")
        break

    ways = [[one, two, three], [four, five, six], [seven, eight, nine], [one, four, seven], [two, five, eight], [three, six, nine], [one, five, nine], [three, five, seven]]
    for element in ways:
        if all(position == "x" for position in element):
            win = True
            board()
            print('WINNER WINNER - "X"')
    
    positions = [one, two, three, four, five, six, seven, eight, nine]
    counter = 0
    for position in positions:
        if position != ' ':
            counter += 1
    if counter == 9:
        print("UNLUCKY")
        break

    
