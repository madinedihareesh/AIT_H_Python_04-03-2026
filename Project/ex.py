name=input('Enter the name:')
username=input('Enter the username: ')
bal=int(input('Enter your bal amount'))
password=input('Enter Password: ')
cpassword=input('confirm password: ')

if password==cpassword:
    print('Rigister successfull')
    

vuname=input('Enter your Username: ')
vpassword=input('Enter your password')

if vuname==username and vpassword==password:
    while True:
        print('1.Withdrawl')
        print('2.Diposit')
        print('3.Bal Enquiry')
        print('4.Logout')
        Choice=int(input('Enter your choice: '))
        match Choice:
            case 1:
                amount=int(input('Enter the amoount to withdraw: '))
                if bal>amount and amount!=0:
                    bal=bal-amount
                    print(f'Your current account bal is: {bal}')
                else:
                    print('Please enter a proper amount')
            case 2:
                amount=int(input('Enter the amount to diposite: '))
                if amount>0:
                    bal=bal+amount
                    print(f'your account current bal: {bal}')
                else:
                    print('Enter a proper amount')
            case 3:
                print(f'Your current account bal {bal}')
            case 4:
                print('Logged Out successfully')
                break                            
                