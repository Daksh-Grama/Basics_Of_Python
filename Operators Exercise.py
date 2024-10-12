'''You and your friends have gone to the Phoenix mall and bought some T-Shirts of Rs 800/- each and trousers of Rs 1500/- each from the Pantaloons showroom. Write a program to find out the total amount payable.'''

'''
number_of_tshirt=int(input("Enter the number of shirts you want to buy:"))
number_of_pants=int(input("Enter the number of pants you want to buy:"))
amount=number_of_pants*1500+number_of_tshirt*800
print("The payable amount for {} t-shirts and {} trouser is {}".format(number_of_tshirt,number_of_pants,amount))'''

'''Now you move on to Cinemax and buy 4 tickets costing Rs 200 /- each for Avengers. You pay Rs 2000/- at the cash counter. Find out how much balance you should be getting.'''
paid=200
no_of_tickets=4
total_cost=no_of_tickets*200
change=2000-total_cost
print("You get {} change".format(change))
friend=int(input("How many friends do you have ."))
share=change/no_of_tickets
print("your friends and you get {} Rs each.".format(share))
