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

#Task 2
#Caluclates the final price of an item when given the price, any discount, and tax rate
def price_calculator (original_price, discount = 0, tax_rate = 0.08) :
    price = round((original_price * (1 - discount)) * (1 + tax_rate), 2)
    return price

#Task 3
#Formats any given string arguments into a single formatted list, with each argument on its own line when printed.
def address_book (*args) :
    combined_addresses = ''
    for arg in args :
        combined_addresses += arg + '\n'
    return combined_addresses

def main() :
    #Task 1 Main
    upper, lower = count_letters('The quick Brow Fox')
    print('The quick Brow Fox')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('')
    print('')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('test')
    print('test')
    print(f"No. of Upper case characters: {upper} \nNo. of Lower case character: {lower}")
    upper, lower = count_letters('TEST')
    print('TEST')
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
    print(address_book("Five", "Quatre", "Tres", "II", "1"))

main()