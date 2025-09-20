import time  # Add this at the very top
Companyname = 'ExampleCorp'



import options  # Import the options module

print("---------------------------------------------------------")


while True:
    for option in options:
        print(option)

    ask1 = input(f"Hello! and Welcome to {Companyname}. How may I help you today? ")

    # option 1
    if ask1 == '1':
        print("We have a variety of products available.")
        prod1 = input("Sure! What product are you interested in? ").lower()
        
        if prod1 == 'product a' or prod1 == 'a':
            import ProductA  # Import the ProductA module
            print(" A is a great choice! We have a wide range of products available.")
        elif prod1 == 'product b' or prod1 == 'b':
            import ProductB  # Import the ProductB module
            print(" B is a popular choice! Let me know if you need more information.")
        elif prod1 == 'product c' or prod1 == 'c':
            import ProductC  # Import the ProductC module
            print(" C is an excellent option! We can help you with that.")
        
        
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating

    # option 2
    elif ask1 == '2':
        help = input("I'm here to help with your order. Please provide your order number or details.")
        if help:
            print(f"Thank you for providing your order details: {help}. We will assist you shortly.")
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating

    # option 3
    elif ask1 == '3':
        know1 = input("Sure! What would you like to know about our services? ")
        print("We offer a range of services including customer support, product installation, and maintenance.")
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating

    # option 4
    elif ask1 == '4':
        feedback = input("Thank you for your willingness to provide feedback. Please share your thoughts:")
        print(feedback)
        print("We appreciate your feedback and will use it to improve our services.")
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating

    # option 5
    elif ask1 == '5':
        print("Please place your order by providing the product name and quantity.")
        products1 = [
    "BIGGYC",
    "HIMONLY"
    "THEMAC"
    "SMOOTHIE"
]
        
        product_name = input("Product Name: ")
        while product_name not in products1:
            print("This products isnt available, please select another one.")
            product_name = input("Product Name: ")
            
        quantity = int(input("Quantity: (Maximum 10, for more, please head to the till.) "))
        print(f"Thank you for your order of {quantity} units of {product_name}. We will process it shortly.")
        if quantity > 10:
            print("Please head to the till.")
            exit()
        else:
            for i in range(1,3):
                print("Loading..")
            
        
        import random
        for i in range(2):
            print("Generating your order number...")
            time.sleep(2)  # Add a short pause for effect
    
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'      
        ordernum = ''
        for x in range(5):
            ordernum += random.choice(chars)
    
        print(f"Your order number is: {ordernum}")
        
        time.sleep(5)  # This pauses before showing the menu again

    # option 6 (exit)
    elif ask1 == '6':
        cntdts = input("Would you like to give your contact details? (yes/no) ").lower()
        if cntdts.lower() == 'yes':
            import contact  # Import the contact module
            print("Thank you for providing your contact details.")
        else:
            print("Thank you for visiting us. Have a great day!")
            exit()
            
    # option 7
    elif ask1 == '7':
        print("Thank you for asking! My day is going well, and I hope yours is too!")
        print(f"If it isn't, {Companyname} is here to help make it better!")
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating

    else:
        print("Invalid option. Please try again.")
        time.sleep(5)  # Add this line to pause for 5 seconds before re-iterating
            
            
            
            
