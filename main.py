from GHORS import *


def main_menu():
    clear()
    main_menu_text = """
        .-.    __
    |   |  /\ 
    |   |  \_\/      __        .-.
    |___|        __ /\ \      /:::
    |:::|       / /\\_\/     /::::/
    |:::|       \/_/        / `-:/
    ':::'__   _____ _____  /    /
        / /\ /     |:::::\ \   /
        \/_/ \     |:::::/  `"`
    jgs     __ `
        /\ 
        \_\/
    
    1. Patients
    2. Doctors
    3. Exit
    
    :: please select a number : """
    choose = input(main_menu_text)

    match (choose):
        case "1":
            patients_menu()

        case "2":
            doctors_menu()

        case _:
            pass


def patients_menu():
    clear()
    patients_menu_text = """
    1. create new patient
    2. delete a patient
    3. edit patient info
    4. show patients of a doctor
    5. show all patients
    0. back to previous menu
    e. exit from app
    
    :: please select number : """

    choose = input(patients_menu_text)
    match (choose):
        case "1":
            pass

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "5":
            pass

        case "0":
            pass

        case "e":
            pass

        case _:
            pass


def doctors_menu():
    clear()
    doctors_menu_text = """
    1. create new doctor
    2. delete a doctor
    3. edit doctor info
    4. search a doctor
    5. show doctors list
    6. show doctors by Expertise
    0. back to previous menu
    e. exit from app
    
    :: please select number : """

    choose = input(doctors_menu_text)
    match (choose):
        case "1":
            pass

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "5":
            pass

        case "6":
            pass

        case "0":
            pass

        case "e":
            pass

        case _:
            pass


main_menu()
