from Manager import File
import os
from colorama import Fore, Style, init  # type: ignore

# test commit
clear = lambda: os.system("cls")
len_Flag = lambda x: True if len(x) == 10 else False
exit_flag = lambda x, Type="Patients": x not in FM.read()[Type]
numric_flag = lambda x: x.isnumeric()

bye = lambda: print("Bye Baby ! ❤️")


def goto_menu():
    choose = input("\nPress Any Key to Back Previous menu or 0 to Exit app : ")
    if choose != "0":
        clear()
    else:
        bye()
        exit()


init(autoreset=True)
FM = File()
if os.path.isfile("database.json") == False:
    FM.create(fileName=None, content={"Patients": {}, "Doctors": {}}, jsonEncode=True)


class Patient(File):
    def __init__(self, Path="database.json"):
        super().__init__(Path=Path)

    def __str__(self):
        return "this class help to working with files in hospital"

    def create(self):
        clear()
        data = super().read()
        itSave = False

        while itSave == False:
            National_Code = input("please input National Code : ")
            if (
                len_Flag(National_Code)
                and exit_flag(National_Code)
                and numric_flag(National_Code)
            ):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")
                Doctor_Code = input("please input Doctor Code (split with ,): ")

                data["Patients"][National_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Code": Doctor_Code.split(","),
                }

                super().write(data)

                itSave = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The patient was successfully created ."
                )
            elif exit_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This national code not found !!!")
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be integer !!!")
        itSave = False

    def delete(self):
        clear()
        data = super().read()
        itSave = False
        while itSave == False:
            National_Code = input("please input National Code : ")

            if not exit_flag(National_Code):
                delete_flag = ""
                while delete_flag != "y" or delete_flag != "n":
                    clear()
                    print("National Code : " + National_Code)
                    print(
                        "First Name : " + data["Patients"][National_Code]["First Name"]
                    )
                    print("Last Name : " + data["Patients"][National_Code]["Last Name"])
                    print(
                        "Doctor Code : "
                        + data["Patients"][National_Code]["Doctor Code"]
                    )
                    delete_flag = input("\n Are you sure to delete? (y/n)")
                    if delete_flag == "y":
                        del data["Patients"][National_Code]
                        super().write(data)
                        itSave = True
                        clear()
                        print(
                            Style.BRIGHT
                            + Fore.GREEN
                            + "The patient was successfully deleted ."
                        )
                        break
                    else:
                        clear()
                        print(
                            Style.BRIGHT
                            + Fore.GREEN
                            + "The patient was canceled deleting ."
                        )
                        break

            elif exit_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This national code already exists !!!")
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be integer !!!")
        itSave = False

    def edit(self):
        clear()
        data = super().read()
        itSave = False
        while itSave == False:
            National_Code = input("please input National Code : ")

            if not exit_flag(National_Code):
                First_Name = input("please input First Name : ")
                Last_Name = input("please input Last Name : ")
                Doctor_Code = input("please input Doctor Code : ")

                data["Patients"][National_Code] = {
                    "First Name": First_Name,
                    "Last Name": Last_Name,
                    "Doctor Code": Doctor_Code.split(","),
                }

                super().write(data)

                itSave = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The patient was successfully edited ."
                )
            elif not exit_flag(National_Code):
                clear()
                print(Fore.YELLOW + "This national code already exists !!!")
            elif not len_Flag(National_Code):
                clear()
                print(
                    Fore.YELLOW
                    + "The length of the national code must be ten characters !!!"
                )
            elif not numric_flag(National_Code):
                clear()
                print(Fore.YELLOW + "The Type of the national code must be integer !!!")
        itSave = False

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
            for id in data["Patients"][National_Code]["Doctor Code"]:
                Doctor_id_str += id + ", "

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


class Doctors(File):
    def __init__(self, Path="database.json"):
        super().__init__(Path=Path)

    def create(self):
        clear()
        data = super().read()
        itSave = False

        while itSave == False:
            Doctor_Code = input("please input Doctor Code : ")
            if exit_flag(Doctor_Code, "Doctors") and numric_flag(Doctor_Code):
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

                itSave = True
                clear()
                print(
                    Style.BRIGHT + Fore.GREEN + "The Doctor was successfully created ."
                )
            elif exit_flag(Doctor_Code):
                clear()
                print(Fore.YELLOW + "This Doctor code not valid !!!")
            elif not numric_flag(Doctor_Code):
                clear()
                print(Fore.YELLOW + "The Type of the Doctor code must be integer !!!")
        itSave = False
