#basic python flow control

print("Flow Control ")
print("You have to go out")
print()
rain = input("Is it raining? (yes or no) : ").lower()
if rain == "no":
    print("You can go outside.")
else:
    umbrella = input("Do you have an umbrella? (yes or no) :").lower()
    if umbrella == "no":
        print("Wait a while")
        rain2 = input("Is it still raining? (yes or no) : ").lower()
        while rain2 =="yes":
            print("Wait a while")
            rain2 = input("Is it still raining? (yes or no) : ").lower()
        print("You can go outside")
    else:
        print("You can go outside using the umbrella")
