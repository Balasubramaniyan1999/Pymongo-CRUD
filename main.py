import pymongo
import re

# credentials to mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["crud"]
mycol = mydb["useraccount"]


# show data
def show_data():
    cursor = mycol.find({},{'_id':0})
    for i in cursor:
        print(i)

# add data
def add_data(username,password):
    mycol.insert_one({'username':username,'password':password})
    print("username and password added successfully")

# delete data
def delete_data(username):
    mycol.delete_one({'username':username})
    print("Deleted the user data successfully")

# Update Password
def update_password(username,password):
    mycol.update_one({'username':username},{'$set':{'password':password}})
    print("Data updated successfully")




if __name__ == '__main__':
    print("1.show data" "\n" "2.Add data" "\n" "3.Delete data" "\n"  "4.Update password")
    user_input = int(input("Enter the operations to do : "))
    if user_input == 1:
        show_data()
    elif user_input == 2:
        print("*********Type Details to add the data*************")
        name = input("Enter the name : ")
        pas = input("Enter the password : ")
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, pas)
        if mat:
            add_data(name,pas)
            show_data()
        else:
            print('password is invalid' '\n' 'password must contains numbers,small case,upper cae,special characters')

    elif user_input == 3:
        show_data()
        print("*********Type username to delete the data********")
        name = input("Enter the name : ")
        delete_data(name)
        print("********After Deletion*******************")
        show_data()
    elif user_input == 4:
        show_data()
        print("************Type New password to update password")
        username = input("Enter the name : ")
        password = input("Enter the New password : ")
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat:
            update_password(username,password)
            print("************After Password Update**********")
            show_data()
        else:
            print('password is invalid' '\n' 'password must contains numbers,small case,upper cae,special characters')


    else:
        print("exit")




