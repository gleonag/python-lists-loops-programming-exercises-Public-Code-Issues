contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
def new_contact(contact):
    for i in contact:
        return(i)
    return new_contact(contact)
print({new_contact(contact)})