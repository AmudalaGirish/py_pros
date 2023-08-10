"""
Email validation based on string usage
"""

# User input 
email = input("Enter Your Email:")

k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="." or i=="_" or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Email address should not have any space or no upper case or no symbols")
            else:
                print("Email should have '.' representation")
        else:
            print("Email address should have @ symbol")
    else:
        print("First letter should start with alphabet")
else:
    print("Email address should be more than 6 letters")