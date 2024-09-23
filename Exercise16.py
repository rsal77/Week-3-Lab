print('Reboot the computer and try to connect')
rebootComp = input('Did that fix the problem? (yes/no): ')

if rebootComp == "no":
    print('Reboot the router and try to connect')
    rebootRout = input('Did that fix the problem? (yes/no): ')
    
    if rebootRout == "no":
        print("Make sure all cables are connected properly.")
        cable = input('Did that fix the problem? (yes/no): ')

        if cable == "no":
            print("Move the router to a new location and try to connect.")
            moveRout = input('Did that fix your problem? (yes/no)')

            if moveRout == "no":
                print("Get a new router.")







