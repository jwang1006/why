from datetime import date
import json

cost_of_class = 5

def new_semester() -> None:
    with open("all_classes.txt", 'r') as f:
        f.read()
        print(f)
    name_list_to_classes_taken()
    


def simulate_class(classname: str) -> None:
    pass


def name_list_to_classes_taken() -> None:
    with open('classes_taken.json', 'w') as f:
        pass

def get_classes_taken(student_name: str): 
    """Returns classes taken by student"""
    pass

def get_amount_paid(student_name: str):
    pass

def get_amount_total(student_name: str):
    pass
def get_amount_owed(student_name: str):
    pass


""""
Name:
    Beg. Hiphop
        Classes Taken: 1
        Dates:
            5/1: True
            5/7: False
    Adv. Hiphop
    Int. Contemporary
    Adv. Contemporary
    Beg. Ballet
    Adv. Ballet


"""