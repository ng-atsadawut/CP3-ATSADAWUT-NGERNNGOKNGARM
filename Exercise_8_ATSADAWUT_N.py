username = input("Username : ")
password = input("Password : ")

userAdmin = "admin"
passAdmin = "test1234!"

espressoPrice = 40
americanoPrice = 35
cremePrice = 40
lattePrice = 50
cappuccinoPrice = 55
mochaPrice = 50
coffee = ""
price = 0

if username == userAdmin:
    if password == passAdmin:
        print("============= Welcome to my shop =============")
        print("")
        print("============= Coffee list =============")
        print("1.Espresso 	    ", espressoPrice, " Bath")
        print("2.Americano 	", americanoPrice, " Bath")
        print("3.Creme 		", cremePrice, " Bath")
        print("4.Latte 		", lattePrice, " Bath")
        print("5.Cappuccino	", cappuccinoPrice, " Bath")
        print("6.Mocha 		", mochaPrice, " Bath")
        print("========================================")
        coffee = input("Please select coffee : ")
        if coffee == "1":
            coffee = "Espresso"
            price = espressoPrice
        elif coffee == "2":
            coffee = "Americano"
            price = americanoPrice
        elif coffee == "3":
            coffee = "Creme"
            price = cremePrice
        elif coffee == "4":
            coffee = "Latte"
            price = lattePrice
        elif coffee == "5":
            coffee = "Cappuccino"
            price = cappuccinoPrice
        elif coffee == "6":
            coffee = "Mocha"
            price = mochaPrice
        else:
            print("You have selected the wrong product.")

        quantity = int(input("How many cup do you want ? : "))

        print("Total :", quantity * price, "Bath")
    else:
        print("Incorrect password.")
else:
    print("Username not found in the system.")


