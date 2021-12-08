name = input()
password = input()
input_password = input()
while input_password != password:
    input_password = input()
print(f"Welcome {name}!")
