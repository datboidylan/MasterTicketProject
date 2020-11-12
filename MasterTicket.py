'''By: Dylan Lafferty

This will be a program that allows a user to purchase tickets for a concert, gig, etc.

'''

ticketPrice = 10

ticketsRemaining = 100

#Run code until out of tickets
while ticketsRemaining >= 1:
    #Output the amount of tickets remaining using ticketsRemaining Variable

    print('There are {} tickets remaining!'.format(ticketsRemaining))

    #Gather the users name and assign it to a new variable

    usersName = input('What is your name?   ')

    #Prompt user how many tickets they would like

    ticketsRequested = input('Hello {}, how many tickets would you like to purchase?   '.format(usersName))

    #Expect a ValueError and handle it so that it catches it
    try:
        ticketsRequested = int(ticketsRequested)
        #Raise a ValueError if more tickets are Requested than Available
        if ticketsRequested > ticketsRemaining :
            raise ValueError("There are only {} tickets available...".format(ticketsRemaining))
    except ValueError as err:
        #Include the Error text in the output

        print("Uh-oh! We ran into an Issue. {} Please Try again".format(err))

    #Let user know how much the tickets together will cost

    #Only have this code run if the try statement is true
    else:
        ticketCost = ticketsRequested * ticketPrice
        print("The total price of the tickets is ${}".format(ticketCost))

        #Promt user if they want to proceed

        userChoice = input("Do you wish to proceed with your Purchase? (Y/N)   ")

        #If they want to proceed
            #Print out to screen "Sold!"
            #Reduce ticketsRemaining by number of Tickets Purchased.

        if(userChoice.lower() == "yes" or userChoice.lower() == "y"):
            print("Sold!")

            ticketsRemaining -= ticketsRequested

        #If they do not want to proceed
            #Thank Them by name 
        elif (userChoice.lower() == "no" or userChoice.lower() == "n"):
            print("Thank you {} for visiting!".format(usersName))

        else:
            print("ERROR: Invalid Input [App Restarting]")


    #Let the user know the tickets are sold out
print("Sorry the tickets are all sold out :(") 