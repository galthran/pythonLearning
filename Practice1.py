password = "pass123"
answer = ""
numberOfTries = 0
maxNumberOfTries = 4
maxTries = "Not reached"

while password != answer and maxTries != "Reached":
    if numberOfTries < maxNumberOfTries:
        answer = input("Provide your password: ")
        numberOfTries = numberOfTries + 1
    else:
        maxTries = "Reached"

if maxTries == "Reached":
    print("Account blocked")
else:
    print("Access granted")