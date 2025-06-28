print("Entry Contact details")
name = input("What is your name? ")
email = input("What is your email address? ")
while '@' not in email or '.' not in email:
    print("Please enter a valid email address.")
    email = input("What is your email address? ")
phone = input("What is your phone number? ")
while not phone.isdigit() or len(phone) < 10:
    print("Please enter a valid phone number (at least 10 digits).")
    phone = input("What is your phone number? ")
print("Thank you for your details.")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Thank you for reaching out, " + name + "!")
print("You will soon receive a confirmation email at", email)
print("Thank you for contacting us, have a great day!")
import time
time.sleep(5)  # Add this line to pause for 5 seconds before exiting