class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Name cannot be empty')
        self.name = name
        
        self.house = house
        
def main():
    student = get_student()
    print(f'{student.name} from {student.house}') 
           
def get_student():
    name = input('Enter your name: ')
    house = input('Enter your house: ')
    return Student(name, house)

if __name__ == '__main__':
    main()