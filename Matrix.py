x = [[]]
x = [[ 0 for i in range(4)] for i in range(3)]
print(x)

for i in x:
    i.insert(0, input('Enter process name: '))
    i.insert(1, float(input("Enter Arrival time: ")))
    i.insert(2, float(input("Enter Execute time: ")))
    print("#########NEXT PROCESS#########")
print(x)
