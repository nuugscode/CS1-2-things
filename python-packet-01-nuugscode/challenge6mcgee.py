print("Oh no mr mcgee has been infected with a zombie virus. He is spreading his virus throughout grant. Test below to see how many people have been infected.")

rate = int(input("rate of infection: "))
days = int(input(" days since infection: "))

peopleinfected = (1 + rate) ** days

print("After " + str(days) + " days, around " + str(peopleinfected) + " people have been infected with the virus.")
