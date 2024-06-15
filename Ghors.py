from Manager import File
import os
from colorama import Fore, Style, init  # type: ignore

# test commit
FM = File()
clear = lambda: os.system("cls")
len_Flag = lambda x: True if len(x) == 10 else False
space_flag = lambda x, Type="Patients": x not in FM.read()[Type]
numric_flag = lambda x: x.isnumeric()
bye = lambda: print("Bye Baby !")


def goto_menu():
    choose = input("\nPress any key for menu, 0 to exit. ... ")
    if choose != "0":
        clear()
    else:
        bye()
        exit()


def dr_numeric_flag(Dr_Code):
    if Dr_Code.isnumeric():
        return True
    elif "," in Dr_Code:
        dr_code_split = Dr_Code.split(",")
        dr_numric_counter = 0
        for number in dr_code_split:
            if number.isnumeric():
                dr_numric_counter += 1

        if len(dr_code_split) == dr_numric_counter:
            return True
        else:
            return False
    else:
        print("no ok")
        return True


def AvDoctor(Doctor_Code):
    Doctor_Codes = Doctor_Code.split(",")
    data = FM.read()
    couner = 0
    len_Doctor = len(Doctor_Codes)

    for Doctor_Code in Doctor_Codes:
        if Doctor_Code in data["Doctors"]:
            couner += 1

    if couner == len_Doctor:
        return True
    else:
        return False


init(autoreset=True)
if os.path.isfile("database.json") == False:
    FM.create(fileName=None, content={"Patients": {}, "Doctors": {}}, jsonEncode=True)


class Patient(File):
    def __init__(self, Path="database.json"):
        super().__init__(Path=Path)

    def __str__(self):
        return "This file helps you manage patient information"

    def create(self):
        clear()
        data = super().read()
        itSaved = False

        while itSaved == False:
            National_Code = input("please input National Code : ")
            if (
                len_Flag(National_Code)
                and space_flag(National_Code)
                and numric_flag(National_Code)
            ):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")
                itDoctor = False

                while itDoctor == False:
                    Doctor_Code = input("please input Doctor Code (split with ,): ")
                    if dr_numeric_flag(Doctor_Code) and AvDoctor(Doctor_Code):
                        itDoctor = True
                    elif not dr_numeric_flag(Doctor_Code):
                        # clear()
                        print(Fore.YELLOW + "Doctor code must be a numeric value !!!")

                    elif not AvDoctor(Doctor_Code):
                        clear()
                        print(
                            Fore.YELLOW
                            + "This code of doctor / doctors is not available in the database !!!"
                        )

                data["Patients"][National_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Code": Doctor_Code.split(","),
                }

                super().write(data)

                itSaved = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The patient was successfully created ."
                )
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be numric !!!")

            elif not space_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This national code duplicate !!!")

        itSaved = False

    def delete(self):
        clear()
        data = super().read()
        itSaved = False
        while itSaved == False:
            National_Code = input("please input National Code : ")

            if not space_flag(National_Code):
                delete_flag = ""
                while delete_flag != "y" or delete_flag != "n":
                    Doctor_id_str = ""
                    for Id in data["Patients"][National_Code]["Doctor Code"]:
                        Doctor_id_str += Id + ", "
                    clear()
                    print("National Code : " + National_Code)
                    print(
                        "First Name : " + data["Patients"][National_Code]["First Name"]
                    )
                    print("Last Name : " + data["Patients"][National_Code]["Last Name"])
                    print("Doctor Code : " + Doctor_id_str[:-2])
                    delete_flag = input("\n Are you sure to delete? (y/n)")
                    if delete_flag == "y":
                        del data["Patients"][National_Code]
                        super().write(data)
                        itSaved = True
                        clear()
                        print(
                            Style.BRIGHT
                            + Fore.GREEN
                            + "The patient was successfully deleted ."
                        )
                        break
                    clear()
                    print(
                        Style.BRIGHT
                        + Fore.GREEN
                        + "The patient was canceled deleting ."
                    )
                    break
            elif space_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This national code not exists !!!")
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be integer !!!")
        itSaved = False

    def edit(self):
        clear()
        data = super().read()
        itSaved = False
        while itSaved == False:
            National_Code = input("please input National Code : ")

            if not space_flag(National_Code):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")

                itDoctor = False
                while itDoctor == False:
                    Doctor_Code = input("please input Doctor Code (split with ,): ")
                    if dr_numeric_flag(Doctor_Code) and AvDoctor(Doctor_Code):
                        itDoctor = True
                    elif not dr_numeric_flag(Doctor_Code):
                        clear()
                        print(Fore.YELLOW + "Doctor code must be a numeric value !!!")

                    elif not AvDoctor(Doctor_Code):
                        clear()
                        print(
                            Fore.YELLOW
                            + "This code of doctor / doctors is not available in the database !!!"
                        )

                data["Patients"][National_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Code": Doctor_Code.split(","),
                }

                super().write(data)

                itSaved = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The patient was successfully edited ."
                )
            elif space_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This doctor code is not available !!!")
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be integer !!!")
        itSaved = False

    def search_patients(self):
        clear()
        data = super().read()

        docid = input("please input doctor id : ")
        clear()

        patient_dict = {}
        patient_exit = False
        for National_Code in data["Patients"]:
            Doctor_id_str = ""
            if docid in data["Patients"][National_Code]["Doctor Code"]:
                for id in data["Patients"][National_Code]["Doctor Code"]:
                    Doctor_id_str = id + ", "
                patient_exit = True
                patient_dict[
                    data["Patients"][National_Code]["First Name"]
                    + " "
                    + data["Patients"][National_Code]["Last Name"]
                ] = [National_Code, Doctor_id_str[:-2]]

        if patient_exit:
            sorted(patient_dict)
            print(
                "{:<15} | {:<15} | {:<15}".format(
                    "Full Name", "National Code", "Doctor Code"
                )
            )
            print("-" * 50)
            for FullName, UserInfo in patient_dict.items():
                print(
                    "{:<15} | {:<15} | {:<15}".format(
                        FullName, UserInfo[0], UserInfo[1]
                    )
                )

    def view_all_patients(self):
        clear()
        data = super().read()

        patient_dict = {}
        patient_exit = True if data["Patients"] != False else False
        for National_Code in data["Patients"]:
            Doctor_id_str = ""
            for Id in data["Patients"][National_Code]["Doctor Code"]:
                Doctor_id_str += Id + ", "

            patient_dict[
                data["Patients"][National_Code]["First Name"]
                + " "
                + data["Patients"][National_Code]["Last Name"]
            ] = [National_Code, Doctor_id_str[:-2]]

        if patient_exit:
            patient_dict_keys = sorted(patient_dict)

            print(
                "{:<15} | {:<15} | {:<15}".format(
                    "Full Name", "National Code", "Doctor Code"
                )
            )
            print("-" * 50)
            for patient_fullname_key in patient_dict_keys:
                print(
                    "{:<15} | {:<15} | {:<15}".format(
                        patient_fullname_key,
                        patient_dict[patient_fullname_key][0],
                        patient_dict[patient_fullname_key][1],
                    )
                )


class Doctors(File):
    def __init__(self, Path="database.json"):
        super().__init__(Path=Path)

    def create(self):
        clear()
        data = super().read()
        itSaved = False

        while itSaved == False:
            Doctor_Code = input("please input Doctor Code : ")
            if space_flag(Doctor_Code, "Doctors") and numric_flag(Doctor_Code):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")

                Doctor_Number = 0
                Phone_Approve = False
                while Phone_Approve == False:
                    Doctor_Number = input("please input Number : ")
                    if (
                        Doctor_Number[:2] == "09"
                        and Doctor_Number.isnumeric()
                        and len(Doctor_Number) == 11
                    ):
                        Phone_Approve = True
                    elif Doctor_Number[:2] != "09":
                        print(
                            Fore.YELLOW
                            + "The first 2 characters must start with 09 or your country is not supported !!!"
                        )
                    elif not Doctor_Number.isnumeric():
                        print(
                            Fore.YELLOW + "The phone number must be a numeric value !!!"
                        )
                    elif len(Doctor_Number) != 11:
                        print(
                            Fore.YELLOW
                            + "The length of the phone number must be 11 characters !!!"
                        )

                Work_types = ["Heart", "Eye", "Children", "General"]
                Work_type_Approve = False
                Work_type = 0
                while Work_type_Approve == False:
                    Work_type = int(
                        input(
                            """
1. Heart
2. Eye
3. children
4. General

please input work type : """
                        )
                    )

                    if 1 <= Work_type <= 4:
                        Work_type_Approve = True

                    else:
                        clear()
                        "your choosed number not valid"

                data["Doctors"][Doctor_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Number": Doctor_Number,
                    "Work Type": Work_types[Work_type - 1],
                }

                super().write(data)

                itSaved = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The Doctor was successfully created ."
                )
            elif not space_flag(Doctor_Code, "Doctors"):
                clear()
                print(Fore.YELLOW + "This Doctor code  is exit!!!")
            elif not numric_flag(Doctor_Code):
                clear()
                print(Fore.YELLOW + "The Type of the Doctor code must be numric !!!")
        itSaved = False

    def delete(self):
        clear()
        data = super().read()
        itSaved = False

        while itSaved == False:
            Doctor_Code = input("please input Doctor Code : ")
            if not space_flag(Doctor_Code, "Doctors") and numric_flag(Doctor_Code):
                clear()
                delete_flag = False
                while delete_flag == False:
                    print("Doctor code : " + Doctor_Code)
                    print("First Name : " + data["Doctors"][Doctor_Code]["First Name"])
                    print("Last Name : " + data["Doctors"][Doctor_Code]["Last Name"])
                    print(
                        "Phone Number : "
                        + data["Doctors"][Doctor_Code]["Doctor Number"]
                    )
                    print("Work Type : " + data["Doctors"][Doctor_Code]["Work Type"])
                    delete_choose = input(
                        "\n Are you sure to deleting Docotor Data (y/n)?"
                    )
                    if delete_choose == "y":
                        clear()
                        del data["Doctors"][Doctor_Code]

                        print(Fore.GREEN + Doctor_Code + " delete success")

                        for National_Code in data["Patients"]:
                            if (
                                Doctor_Code
                                in data["Patients"][National_Code]["Doctor Code"]
                            ):
                                data["Patients"][National_Code]["Doctor Code"].remove(
                                    Doctor_Code
                                )
                        super().write(data)
                        delete_flag = True
                        itSaved = True
                    elif delete_choose == "n":
                        print("deleting Doctor Code Has been canceled !!!")
                        break
                    else:
                        print("please try again to choose !")
            elif space_flag(Doctor_Code):
                print("this Doctor Code Not exit ! ")

    def edit(self):
        clear()
        data = super().read()
        itSaved = False

        while itSaved == False:
            Doctor_Code = input("please input Doctor Code : ")
            if not space_flag(Doctor_Code, "Doctors") and numric_flag(Doctor_Code):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")

                Doctor_Number = 0
                Phone_Approve = False
                while Phone_Approve == False:
                    Doctor_Number = input("please input Number : ")
                    if (
                        Doctor_Number[:2] == "09"
                        and Doctor_Number.isnumeric()
                        and len(Doctor_Number) == 11
                    ):
                        Phone_Approve = True
                    elif Doctor_Number[:2] != "09":
                        print(
                            Fore.YELLOW
                            + "The first 2 characters must start with 09 or your country is not supported !!!"
                        )
                    elif not Doctor_Number.isnumeric():
                        print(
                            Fore.YELLOW + "The phone number must be a numeric value !!!"
                        )
                    elif len(Doctor_Number) != 11:
                        print(
                            Fore.YELLOW
                            + "The length of the phone number must be 11 characters !!!"
                        )

                Work_types = ["Heart", "Eye", "Children", "General"]
                Work_type_Approve = False
                Work_type = 0
                while Work_type_Approve == False:
                    Work_type = int(
                        input(
                            """
1. Heart
2. Eye
3. children
4. General

please input work type : """
                        )
                    )

                    if 1 <= Work_type <= 4:
                        Work_type_Approve = True

                    else:
                        clear()
                        "your choosed number is not valid"

                data["Doctors"][Doctor_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Number": Doctor_Number,
                    "Work Type": Work_types[Work_type - 1],
                }

                super().write(data)

                itSaved = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The Doctor was successfully edited ."
                )
            elif space_flag(Doctor_Code):
                clear()
                print(Fore.YELLOW + "This Doctor code not valid !!!")
            elif not numric_flag(Doctor_Code):
                clear()
                print(Fore.YELLOW + "The Type of the Doctor code must be integer !!!")
        itSaved = False

    def search_doctor(self):
        clear()
        data = super().read()
        itSearched = False

        while itSearched == False:
            Doctor_Code = input("please input Doctor Code : ")
            if not space_flag(Doctor_Code, "Doctors") and numric_flag(Doctor_Code):
                for docid in data["Doctors"]:
                    if docid == Doctor_Code:
                        print("Doctor Code : " + Doctor_Code)
                        print(
                            "First Name : " + data["Doctors"][Doctor_Code]["First Name"]
                        )
                        print(
                            "Last Name : " + data["Doctors"][Doctor_Code]["Last Name"]
                        )
                        print(
                            "Phone Number : "
                            + data["Doctors"][Doctor_Code]["Doctor Number"]
                        )
                        print(
                            "Work Type : " + data["Doctors"][Doctor_Code]["Work Type"]
                        )
                        itSearched = True

    def view_all_doctors(self):
        clear()
        data = super().read()
        doctor_dict = {}

        if len(data["Doctors"]) != 0:
            for Doctor_Code_data in data["Doctors"]:
                doctor_dict[
                    data["Doctors"][Doctor_Code_data]["First Name"]
                    + " "
                    + data["Doctors"][Doctor_Code_data]["Last Name"]
                ] = [
                    Doctor_Code_data,
                    data["Doctors"][Doctor_Code_data]["Doctor Number"],
                    data["Doctors"][Doctor_Code_data]["Work Type"],
                ]

            doctor_dict_keys = sorted(doctor_dict)
            print(
                "\n{:<15} | {:<15} | {:<15} | {:<10}".format(
                    "Full Name", "Doctor Code", "Phone Number", "Work Type"
                )
            )
            print("-" * 65)

            for docId in doctor_dict_keys:
                print(
                    "{:<15} | {:<15} | {:<15} | {:<10}".format(
                        docId,
                        doctor_dict[docId][0],
                        doctor_dict[docId][1],
                        doctor_dict[docId][2],
                    )
                )

    def view_all_doctors_by_type(self):
        clear()
        data = super().read()
        Work_types = ["Heart", "Eye", "Children", "General"]
        finded = {"Heart": [], "Eye": [], "Children": [], "General": []}

        for Type in Work_types:
            for Doctor_code_data in data["Doctors"]:
                if data["Doctors"][Doctor_code_data]["Work Type"] == Type:
                    finded[Type].append(Doctor_code_data)

            if len(finded[Type]) != 0:
                print(
                    Fore.LIGHTYELLOW_EX + f"\n{'=' * 25} Work Type: {Type} {'=' * 25}\n"
                )
                print(
                    "{:<20} | {:<15} | {:<15} | {:<10}".format(
                        "Full Name", "Doctor Code", "Phone Number", "Work Type"
                    )
                )
                print("-" * 67)

                for Doctor_code_data in finded[Type]:
                    first_name = data["Doctors"][Doctor_code_data]["First Name"]
                    last_name = data["Doctors"][Doctor_code_data]["Last Name"]
                    full_name = f"{first_name} {last_name}"

                    print(
                        "{:<20} | {:<15} | {:<15} | {:<10}".format(
                            full_name,
                            Doctor_code_data,
                            data["Doctors"][Doctor_code_data]["Doctor Number"],
                            data["Doctors"][Doctor_code_data]["Work Type"],
                        )
                    )
                print("\n")
