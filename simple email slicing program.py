# simple email slicing

email = input("Enter your email: ")

# from 0 index slice to @ sign without @ sign
username = email[:email.index("@")]  
# after @ sign will slice   
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")