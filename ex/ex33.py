# i = 1
# numbers = []
#
# while i < 6:
#     print(f"At the top i is  {i}")
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#     print("The numbers: ")
#
# for num in numbers:
#     print(num)


# def while_loop(end_point=1, j=1):
#     numbers = []
#     i = 1
#     while i < end_point:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#
#         i += j
#         print(f"Numbers now: ", numbers)
#         print(f"At bottom i is {i}")
#
#
# while_loop(8, 2)
# numbers = []
#
# for num in numbers:
#     print(num)

def loop_func(begin, end, j):
    numbers = []
    for i in range(begin, end, j):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At bottom i is {i}")


loop_func(1, 14, 2)
