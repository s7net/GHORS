from Ghors import *


def menu():
    while True:
        clear()
        menuText = """ 
    .-.    __
    |   |  /\ \\     ~ GHORS
    |   |  \_\/      __        .-.
    |___|        __ /\ \      /:::\\
    |:::|       / /\_\/      /::::/
    |:::|       \/_/        / `-:/
    ':::'__   _____ _____  /    /
        / /\ /     |:::::\ \   /
        \/_/ \_____|:::::/  `"`

    1. Patients
    2. Doctors 
    e. Exit
        
    Please Select Number : """
        choose = input(menuText)

        match (choose):
            case "1":
                clear()
                PatientMenu()

            case "2":
                clear()
                DoctorMenu()

            case "e":
                clear()
                bye()
                exit()


def PatientMenu():
    patient = Patient()
    while True:
        PatientText = """ 
        1. create a new user
        2. delete a user
        3. edit a user 
        4. view users of a doctor
        5. view all users
        0. back to main
        e. Exit

        Please Select Number : """
        choose = input(PatientText)
        match (choose):

            case "1":  # create a new user
                patient.create()

            case "2":  # delete a user
                patient.delete()

            case "3":  # edit a user
                patient.edit()

            case "4":  # search patient by doctor
                patient.search_patients()
                goto_menu()

            case "5":  # view all patient
                patient.view_all_patients()
                goto_menu()

            case "0":  # back to main menu
                menu()

            case "e":  # exit
                clear()
                bye()
                exit()


def DoctorMenu():
    doctor = Doctors()
    while True:
        DoctorText = """
1. create a new doctor
2. delete a doctor
3. edit a doctor 
4. search a doctor
5. view all doctors
6. show doctors by cert
0. back to main

please select a number : """
        choose = input(DoctorText)

        match (choose):
            case "1":
                clear()
                doctor.create()

            case "2":
                clear()
                doctor.delete()


menu()
