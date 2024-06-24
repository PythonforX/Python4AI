# Function is a block of reusable code

# def greet(name):
#     print(f"Hello {name}")

# greet("rohan")
# greet("rahul")
# greet("john")

# def area(width, height):
#     area = width * height
#     print(f"Area is {area}")

# area(45,70)
# area(40,70)
# area(41,90)

def pizza_order(size, *toppings):
    print(f"Size of the pizza : {size}")
    for i in toppings:
        print(i)

pizza_order(12,"tomato","mushrooms","green peppers")








