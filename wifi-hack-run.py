import time
import random
import string


def generate_fake_address():
    # Random house number
    house_number = random.randint(1, 9999)

    # Random street name
    street_names = ["Maple", "Oak", "Pine", "Elm", "Cedar", "Birch", "Willow", "Main", "High", "Washington"]
    street_types = ["St", "Ave", "Blvd", "Ln", "Rd", "Dr", "Pl"]
    street_name = random.choice(street_names) + " " + random.choice(street_types)

    # Random city and state
    cities = ["Springfield", "Rivertown", "Lakeside", "Hillview", "Sunnyvale", "Brookside"]
    states = ["CA", "TX", "NY", "FL", "WA", "OR", "PA", "CO"]
    city = random.choice(cities)
    state = random.choice(states)

    # Random postal code
    postal_code = ''.join(random.choices(string.digits, k=5))

    # Combine into a fake address
    fake_address = f"{house_number} {street_name}, {city}, {state} {postal_code}"

    return fake_address

# Generate and display one random fake address


def generate_fake_proxy():
    protocols = ["http", "https", "socks4", "socks5"]
    tlds = [".com", ".net", ".org", ".io", ".xyz"]

    # Randomly select a protocol
    protocol = random.choice(protocols)

    # Generate a random IP address (fake)
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))

    # Generate a random port (usually between 1024 and 65535)
    port = random.randint(1024, 65535)

    # Generate a random domain name
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))

    # Combine it into a proxy URL
    fake_proxy_url = f"{protocol}://{domain}{random.choice(tlds)}:{port}"

    return fake_proxy_url

# Generate and display 10 random fake proxy URLs
    

print("""
██╗    ██╗██╗███████╗██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║    ██║██║██╔════╝██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██║ █╗ ██║██║█████╗  ██║    ███████║███████║██║     █████╔╝ 
██║███╗██║██║██╔══╝  ██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
╚███╔███╔╝██║██║     ██║    ██║  ██║██║  ██║╚██████╗██║  ██╗
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                            
""")

time.sleep(2)

print('WELCOME TO WIFI HACK!')

a = input("PLEASE ENTER 'Y' TO AGREE TO THE TERMS AND CONDITIONS>>>")

if a == 'Y' or 'y':
    pass

else:
    exit()
    



xa = input("What type of attack you want to Do?")


if xa == "bruteForce":
    pass

else:
    print("Please try again by exting :(")
    
    
    

b = input("Please enter the IP of your device")
print("done!")
time.sleep(1)
print("Fetching a proxy URL: " + generate_fake_proxy ())
print("choosing a locatatoin: " + generate_fake_address ())
n = input('please enter the name of the wifi device you want to connect to: ')
print('Checking if Your Wifi password is strong or not!!....')
time.sleep(5)
print('Oh no!!!, this wifi has a really strong password and it will approximately take longer')
time.sleep(1)

print("it will take 15 minutes to Connect And Hack!!!")
time.sleep(1)
print("please wait while you are connected!")
time.sleep(900)

print(f"WIFI Name = {n}\n WIFI Password: Malik Rajpoot@1")
