#Name: Nikhil Kowdle
#Lab 10
#This program contains the tasks required for this assignment.

def main():
    #Task 1
    list1 = [5, 2, 12, 4, 9, 13, 22, 1, 6, 17]
    print(f"Before: {list1}")
    list1.sort(key=lambda x: -x)
    print(f"After: {list1}\n")
    list2 = list3 = [("Kate", 3), ("Sam", 2), ("Kate", 5), ("Jolly", 1), ("Alp", 2), ("Beta", 3), ("Alp", 1), ("Alpine", 2), ("Sam", 4), ("Bob", 2), ("Sam", 3)]
    print(f"Before: {list2}")
    list2.sort(key=lambda x: x[0])
    print(f"After: {list2}\n")
    print(f"Before: {list3}")
    list3.sort(key=lambda x: -x[1])
    print(f"After: {list3}\n")

    #Task 2
    import random
    list4 = list5 = [random.randint(1, 100) for _ in range(20)]
    print(f"Before: {list4}")
    list4 = list(map(lambda x: x*2 if x%2 == 0 else x**2, list4))
    print(f"After: {list4}\n")
    print(f"Before: {list5}")
    list5 = list(filter(lambda x: False if x%2 == 0 or x%5 == 0 else True, list5))
    print(f"After: {list5}\n")

main()