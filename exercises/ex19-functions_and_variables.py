def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party..")
    print("Get a blanket. \n")


print("Let's give the function numbers directly!")
cheese_and_crackers(20, 30)

print("Or.. Use variables from our scripts.")
amount_of_cheese = 21
amount_of_crackers = 25

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Let's do MATH inside,")
cheese_and_crackers(10 + 20, 21 + 32)

print("We can combine the Math with variables.")
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 34)
