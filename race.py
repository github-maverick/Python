dict={"Usain":1, "Me":2, "Qazi":3}
def choice_to_number(choice):
    return dict[choice]

def number_to_choice(number):
    for x in dict:
        if dict[x]==number:
            return x

usr_choice=input("Person of choice:")
print(choice_to_number(usr_choice))
usr_number=int(input("Number of choice:"))
print(number_to_choice(usr_number))
