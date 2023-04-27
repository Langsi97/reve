z: int = "4"
x: str = "hello"

y = int("4")
w = y + 'a'


def my_sum(a: int, b: int) -> str:
    return str(a) + str(b)


number1 = input("Enter a number:")
number2 = input("Enter a number:")
print(f"The sum is {my_sum(number1,number2)}")

print(c)

# supplying integer arguments
print(my_sum(1, 2))

# supplying string arguments
print(my_sum("Hello", "World"))


def no_return(a: int) -> int:
    print("oops")


def my_return(a: int) -> None:
    return "value"
