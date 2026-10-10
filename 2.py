import time

tasks = {

}
def menu():
    for i in range(5):
        print()
    print("== TO DO LIST ==")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Отметить выполненной")
    print("5. Выйти")













menu()
while True:
    while True:
        try:
            a = int(input("Выбери действие:"))
            break
        except ValueError:
            print("Something went wrong")
    if a == 1:
        print(tasks)
        print("Enter 5 to go back menu!")
        while True:
            try:
                back = int(input())

                while back != 5:
                    back = int(input("??? еще раз:"))

                menu()
                break
            except ValueError:
                print("Error, try again")
    elif a == 2:
        while True:
            try:
                print("Enter 5 to go back menu!")
                addtask = input("Добавьте задачу:")
                if addtask == str(5):
                    menu()
                    break
                tasks.update({addtask: "False"})

            except ValueError:
                print("Something went wrong")
    elif a == 3:
        while True:
            try:
                print("Enter 5 to go back menu!")
                deletetask = input("Что хотите удалить?:")
                if deletetask == str(5):
                    menu()
                    break
                del tasks[deletetask]
                print("Success!")
            except ValueError:
                print("Something went wrong")
            except KeyError:
                print("Couldn't find task!")
                print("List of Tasks:", tasks)
    elif a == 4:
        while True:
            try:
                print("Enter 5 to go back menu!")
                dotask = input("Какую задачу хотите отметить выполненной?:")

                if dotask in tasks:
                    tasks[dotask] = "True"
                    print("Success!")
                elif dotask == str(5):
                    menu()
                    break
                else:
                    print("Couldn't find task!")
                    print("List of Tasks:", tasks)
            except ValueError:
                print("Something went wrong")
            except KeyError:
                print("Couldn't find task!")

    elif a == 5:
        print("There is no more menu Hehehe")
        time.sleep(2)
        menu()
    elif a == 67:
        break


