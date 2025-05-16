# Assignment Part 1

class Patient:
    def __init__(self, id, name, age, blood, next, prev):
        self.id = id
        self.name = name
        self.age = age
        self.blood = blood
        self.next = next
        self.prev = prev


class WRM:
    def __init__(self):
        self.head = Patient(None, None, None, None, None, None)
        self.head.next = self.head
        self.head.prev = self.head

    def registerPatient(self, id, name, age, blood):
        tail = self.head.prev
        newPatient = Patient(id, name, age, blood, self.head, tail)
        tail.next = newPatient
        self.head.prev = newPatient

    def servePatient(self):
        if self.head.next == self.head:
            print("No patient to be served")
            return None
        temp = self.head.next
        print(f"{temp.name} is served.")
        self.head.next = temp.next
        temp.next.prev = self.head
        temp.next, temp.prev = None, None

    def showAllPatient(self):
        if self.head.next == self.head:
            print("No patient in the wrm")
            return None
        temp = self.head.next
        while temp != self.head:
            print(temp.name, end=" ")
            temp = temp.next
        print()

    def canDoctorGoHome(self):
        print("Yes") if self.head.next == self.head else print("No")

    def cancelAll(self):
        if self.head.next != self.head:
            self.head.next = self.head
            self.head.prev = self.head
            print("All appointments cancelled")
        else:
            print("No patient in the wrm")

    def reverseTheLine(self):
        if self.head.next == self.head:
            return self.head

        current = self.head
        while True:
            current.next, current.prev = current.prev, current.next
            current = current.prev
            if current == self.head:
                break
        return self.head


medical = WRM()
print("**Welcome to Waiting Room Management System**")
while True:
    print(f"""==Choose an option==
1. RegisterPaitent()
2. ServePatient()
3. CancelAll()
4. CanDoctorGoHome()
5. ShowAllPaitent()
6. reverseTheLine()
7. exit
=====================""")
    prompt = input("Enter your choice: ")
    if prompt == "1":
        print("executing RegisterPatient()...")
        print()
        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        blood = input("Enter Blood Group: ")
        info = medical.registerPatient(id, name, age, blood)
        print("Success registering patient", end="\n\n")
    elif prompt == "2":
        print("executing ServePatient()...")
        medical.servePatient()
        print()
    elif prompt == "3":
        print("executing CancelAll()...")
        medical.cancelAll()
        print()
    elif prompt == "4":
        print("executing CanDoctorGoHome()...")
        medical.canDoctorGoHome()
        print()
    elif prompt == "5":
        print("executing ShowAllPatient()...")
        medical.showAllPatient()
        print()
    elif prompt == "6":
        medical.reverseTheLine()
        print()
    elif prompt == "7":
        print("Thank You For Using Waiting Room Management System")
        print("EXITING...")
        break
    else:
        print("No Such Option", end="\n\n")
