'''
Design a program to validate email addresses based on several criteria. Your program should take an email address as input and check it against the following rules:

Case Check: Verify if the email address is in lowercase. If not, mark it as failed.
Alpha Check: Ensure that the first character of the email address is an alphabet.
@ Check: Confirm that the email address contains exactly one '@' symbol.
End Withs Check: Validate whether the email address ends with one of the following domain extensions: '.com', '.in', '.global', or '.inc'.
Space Check: Determine if there are any spaces within the email address.
Length Check: Verify that the length of the email address is at least 6 characters.
'''
def check_case(email):
    if (email.lower()) == email:
        print("case check pass")
    else:
        print("case check is failed")

def alpha_check(email):
    if email[0].isalpha():
        print("alpha check is pass")
    else:
        print("alpha check is failed")

def attherate_check(email):
    if email.count('@') == 1:
        print("@ check pass")
    else:
        print("@ check failed")

def endwiths_check(email):
    if (email[-4] == '.com') or(email[-3] == '.in') or (email[-6] == '.global') or (email[-4] == '.inc') :
        print("endwiths check pass")
    else:
        print("endwiths check failed")

def space_check(email):
        if ' ' in email:
            print("space check failed")
        else:
            print("space check pass")

def dot_check(email):
        if '.' in email:
            print("dot check pass")
        else:
            print("dot check failed")

def length_check(email):
    if len(email) >= 6:
        print("length check pass")
    else:
        print("length check failed")

def main():
    email = input("Enter the email Id:-")

    functionlist = [check_case,alpha_check,attherate_check,endwiths_check,space_check,dot_check,length_check]
    for fun in functionlist:
        fun(email)

#main
main()
