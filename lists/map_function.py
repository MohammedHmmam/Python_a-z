#The map() Function executes a specified for each item in an iterable.
##The  item is sent to the function as a parameters
#### Syntax: map(Function , iterable)
############# Parameters :
############################# Function: Required|| - The function to execute for each item
############################# Iterable: Required|| - A sequence, collection or an iterable
###################################################-> You can send as many iterables as like, just make the function
###################################################=> has one parameter for each iterable.


#Example 1
"""
def myFanc(a,b):
    return a+b

x = map(myFanc , ('Apple' , 'Banana' , 'Cherry') , ('Orange' , 'lemon' , 'Tex'))

print(list(x))
"""
#------------------------------------------------------------#
#-------------------------------------------------------------#
""" ---------------------------------------------------- """

#Example 2
""" Consider a situation in which you need to calculate the price after tax for a list of transaction """

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_prices_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = map(get_prices_with_tax , txns)
print(list(final_prices))    

