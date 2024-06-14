from datetime import date
import json
class_dict = {}
cost_of_class = 5

def new_semester() -> None:
    with open("musical/all_classes.txt", 'r') as f:
        all_classes = f.readlines()
        all_classes = [n.strip() for n in all_classes]
    with open("musical/all_names.txt", "r") as f:
        unformatted = f.readlines()
        names = []
        for name in unformatted:
            formatted = name.split()
            if len(formatted) != 0:
                names.append(f"{formatted[0]} {formatted[1]}")
    
    for name in names:
        key_values = {dance_class: {} for dance_class in all_classes}
        key_values["Paid"] = 0
        class_dict[name]=key_values
    print(class_dict)



def add_class_today(class_name: str) -> None:
    for student in class_dict.keys():
        class_dict[student][class_name][str(date.today())]=False


def check_in(student_name, class_name: str) -> None:
    class_dict[student_name][class_name][date.today()]=True


def get_classes_taken(student_name: str): 
    classesTaken = 0
    for class_name in class_dict[student_name]:
        for class_date, taken in class_dict[student_name][class_name].items():
            if taken:
                classesTaken +=1
    return classesTaken

def get_amount_paid(student_name: str):
    return class_dict[student_name]["Paid"][date.today()]

def add_money(student_name: str, amount_of_money: int):
    class_dict[student_name]["Paid"]+=amount_of_money
    

def get_amount_total(student_name: str):
    return get_classes_taken(student_name)*cost_of_class

def get_amount_owed(student_name: str):
    return get_amount_owed()-get_amount_paid()

if __name__ == "__main__":
    with open ("musical/classes_taken.json", "r") as f:
        class_dict = json.load(f)
    print(class_dict)
    add_money("Sarah Bae", 20)
    add_class_today("Beg. Hiphop")
    with open ("musical/classes_taken.json", "w") as f:
        json.dump(class_dict, f)