import random

spreads_file = open("spreads.txt", "r")
sprinkles_file = open("sprinkles.txt", "r")
cookies_file = open("cookies.txt", "w")

spreads = spreads_file.readlines()
num_of_spreads = len(spreads)

sprinkles = sprinkles_file.readlines()
num_of_sprinkles = len(sprinkles)

for x in range(12):
    current_spread = random.randint(0, num_of_spreads - 1)
    current_sprinkle = random.randint(0, num_of_sprinkles - 1)

    cookies_file.write(str(x+1)
        + ". Cookie with spread " + spreads[current_spread]
        + "and on top sprinkles of " + sprinkles[current_sprinkle])

spreads_file.close()
sprinkles_file.close()
cookies_file.close()
