def numberTable(num):
    print("-----------")
    print(f"table of {num}\n")

    for i in range(1,11):
        print(f"{num} * {i} : {num*i}")
    print("----------\n")



for i in range(1,21):
    numberTable(i)
