import sqlite3

con = sqlite3.connect('roomExpense.db', check_same_thread=False)
cur = con.cursor()


def addToDB():
    spenders = input('Who paid? : ')
    cows = input('Who did not? : ')
    amount = int(input('How much? : '))

    spenders = list(spenders)
    cows = list(cows)
    amount /= (len(spenders) + len(cows))

    for i in spenders:
        for j in cows:
            cur.execute(f'INSERT INTO transactions (waster, saver, Amount, isOK) VALUES ({i}, {j}, {amount}, 0)')
            con.commit()


def reset():
    cur.execute('UPDATE transactions SET isOK = 1')
    con.commit()


def getDebts():
    cur.execute('SELECT * FROM transactions')
    if len(cur.fetchall()) < 1:
        print('Nothing to show!')

    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                pass
            else:
                cur.execute(f'SELECT amount FROM transactions WHERE waster = {i} and saver = {j} and isOk = 0')
                debts = cur.fetchall()
                try:
                    test = debts[0][0]
                    sum = 0
                    for k in debts:
                        sum += k[0]
                    print(f'{j} to {i}: ', sum)
                except:
                    pass


def showPeople():
    cur.execute('SELECT * FROM people')
    users = cur.fetchall()
    for i in range(len(users)):
        print(f'{i + 1} = {users[i][1]}')


def addNewUser():
    user = input('Name ? ')
    query = f'INSERT INTO PEOPLE (Username) VALUES ("{user}")'
    cur.execute(query)
    con.commit()
    print('Done!')


print(
    """
Hello
Plz enter your desired option
1. Add new info
2. Reset all debts
3. Get all Debts
4. Help me i dont know  what are numbers in debts!
5. Add new user
6. Exit
"""
)
while True:

    try:
        choice = int(input())
        if choice == 1:
            addToDB()
        elif choice == 2:
            reset()
        elif choice == 3:
            getDebts()
        elif choice == 4:
            showPeople()
        elif choice == 5:
            addNewUser()
        else:
            break
    except:
        print('Enter a valid option!')