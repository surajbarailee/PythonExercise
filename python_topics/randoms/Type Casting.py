x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

print(x, y, z)


x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

print(x, y, z, w)

x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x, y, z)


def percentage_to_number(percentage):
    # 5 = 100% = 5
    # 1 = 20% = 1
    # 2 = 40% = 2
    return percentage / 20


print(percentage_to_number(15.25))
