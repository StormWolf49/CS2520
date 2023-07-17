#Name: Nikhil Kowdle
#Lab 4
#This program contains the 3 tasks required for this assignment.

#Task 1
#Counts each type of letter formatting (uppercase/lowercase) in the string inputted
def count_letters (sentence) :
    upper_case, lower_case = 0, 0
    for e in sentence :
        if e.isupper() :
            upper_case += 1
        elif e.islower() :
            lower_case += 1
    return upper_case, lower_case

'''
Test 1
The quick Brow Fox
No. of Upper case characters: 3 
No. of Lower case character: 12

Test 2

No. of Upper case characters: 0 
No. of Lower case character: 0

Test 3
why are we whispering
No. of Upper case characters: 0 
No. of Lower case character: 18

Test 4
WHY ARE WE SCREAMING
No. of Upper case characters: 17 
No. of Lower case character: 0
'''

#Task 2
#Caluclates the final price of an item when given the price, any discount, and tax rate
def price_calculator (original_price, discount = 0, tax_rate = 0.08) :
    price = round((original_price * (1 - discount)) * (1 + tax_rate), 2)
    return price

'''
Test 1
Original Price: 100, discount 20%, tax rate 8%, final price 86.4

Test 2
Original Price: 523, discount 0%, tax rate 9.5%, final price 572.68

Test 3
Original Price: 250, discount 35%, tax rate 0%, final price 162.5

Test 4
Original Price: 420, discount 69%, tax rate 7%, final price 139.31
'''

#Task 3
#Formats any given string arguments into a single formatted list, with each argument on its own line when printed.
def address_book (*args) :
    combined_addresses = ''
    for arg in args :
        combined_addresses += arg + '\n'
    return combined_addresses

'''
Test 1
Lan Cal Poly Pomona
Kay CSUFullerton
Jane Microsoft

Test 2
John Doe
Jane Doe
The Batman
The Guy in the Broken yet suprisngly Ergonomic Chair
Fred
'''

def main() :
    #Task 1 Main
    upper, lower = count_letters('The quick Brow Fox')
    print('The quick Brow Fox')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('')
    print('')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('why are we whispering')
    print('why are we whispering')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('WHY ARE WE SCREAMING')
    print('WHY ARE WE SCREAMING')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")

    print()
    
    #Task 2 Main
    print(f'Original Price: {100}, discount {20}%, tax rate {8}%, final price {price_calculator(100, 0.2)}')
    print(f'Original Price: {523}, discount {0}%, tax rate {9.5}%, final price {price_calculator(523, tax_rate=0.095)}')
    print(f'Original Price: {250}, discount {35}%, tax rate {0}%, final price {price_calculator(250, 0.35, 0)}')
    print(f'Original Price: {420}, discount {69}%, tax rate {7}%, final price {price_calculator(420, 0.69, 0.07)}')

    print()

    #Task 3 Main
    print(address_book(''))
    print(address_book ("Lan Cal Poly Pomona", "Kay CSUFullerton", "Jane Microsoft"))
    print(address_book("John Doe", "Jane Doe", "The Batman", "The Guy in the Broken yet suprisngly Ergonomic Chair", "Fred "))

main()