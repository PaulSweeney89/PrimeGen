# prime generator program

P = []

for i in range(2, 100):
    isprime = True

    for j in range(2, i):
        if i % j == 0:
            isprime = False
            break

    if isprime:
        P.append(i)

print(P)

# test code
print(3 % 2 == 0) # Returns False -> is Not Prime
print (7 % 7 == 0) # Returns True -> is Prime