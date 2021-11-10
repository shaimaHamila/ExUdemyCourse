person = {
    "Name": "chaima",
    "Gender": "Feminal",
    "Age": "20",
    "Address": "hamilachaima18@gmail.com",
    "Phone": "22016583"
}
key = input("What information do you want to know about the person?\n")
print(person.get(key, "That information is not available !"))
