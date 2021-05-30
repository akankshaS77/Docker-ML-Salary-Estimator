#!/usr/bin/python3
import pandas
import os

os.system('tput setaf 6')
print('`````````````````````````````````````````````````````````')
os.system('tput setaf 4')
print('----------------------Salary Estimator-------------------')
os.system('tput setaf 6')
print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
os.system('tput setaf 9')
passwd=input("Pass Product Key: ")
dataset=pandas.read_csv('dataset.csv')
X=dataset['featureone'].values.reshape(len(dataset['featureone']),1)
y=dataset['Estimation']

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)


while passwd=='redhat':
    os.system('tput setaf 5')
    put=input("""\n\n----(1). Type "Y" to redirect our product
----(2). Type "N" to Exit
>>>Enter Your Choice: """)
    while(put=='Y' or 'y' and 'N' or 'n' ):
        if (put=='Y' or 'y'):
                ele=float(input("\n\nYour Employee's Yr. of Experience: "))
                magic=model.predict([[ele]])
                os.system('tput setaf 2')
                print("Estimated Salary for given Years of Experience is ",magic)
                os.system('tput setaf 9')
                while True:
                    esc=input("""+ 'Enter' to Continue 
+ write 'exit' to Logout
TYPE: """)
                    if esc == 'exit':
                        print()
                        os.system('tput setaf 6')
                        print("\t-----Wish You Great Day!!----")
                        exit()
                    elif esc == "":
                        break
                    else:
                        os.system('tput setaf 1')
                        print("Not Understood!! TYPE AGAIN")
        else:
            os.system('tput setaf 4')
            print('Thanks for using. Remember: Put correct data!')
            os._exit(1)
