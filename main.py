import random

#create list to contain tickets and variable for new tickets
all_tickets = []
new_tickets = ""

#Take user input in the format "StudentName #" for new tickets and add them to the list
while new_tickets != "done":
    try:
        new_tickets = input("Enter student name and ticket count (Format: 'StudentName #')(End with 'done'): ")

        if new_tickets != "done":
            tokens = new_tickets.split()
            tokens[1] = int(tokens[1])

            for ticket in range(0, tokens[1]):
                    all_tickets.append(tokens[0])
        else:
            break
    except:
        print("Enter values in the 'StudentName #' format")

#Display all tickets in the box
print("Tickets in box: ", all_tickets)

#Start drawing tickets using 'd' or 'q'
d_or_q = ""
while d_or_q != "q":
    try:
        if len(all_tickets) > 0:
            d_or_q = input("Enter 'd' to draw or 'q' to quit")

            if d_or_q == 'd':
                random_value = random.randint(0, (len(all_tickets) - 1))
                print(all_tickets[random_value], "wins a prize!")

                #Remove all instances of the winner from the list
                val = all_tickets[random_value]
                try:
                    while True:
                        all_tickets.remove(val)
                except ValueError:
                    pass

            elif d_or_q == 'q':
                print("All prizes have been given out")

            elif d_or_q != 'd' and d_or_q != 'q':
                print("Enter 'd' or 'q'")
        else:
            print("No more tickets")
            break
    except:
        print("Enter 'd' or 'q'")




