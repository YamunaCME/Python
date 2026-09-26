employee = {
    "id":101,
    "name":"yamuna",
    "age":17
}
try:
    x=input("enter key value to search:")
    print(employee[x])
except KeyError as e:
    print("entered detials are not avaliable!")    