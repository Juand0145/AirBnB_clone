#!/usr/bin/python3
'''This is the program that contains the entry point
of the command interpreter'''
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    '''Class that create a console were the commands
    are going to be executed'''
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        ''' Quit program to exit the program'''
        if arg is not None:
            exit()

    def do_EOF(self, arg):
        ''' Quit program to exit the program '''
        if arg is not None:
            exit()

    def verification(self, arguments, mode):
        '''Is a usefull functions to verify if any of argumment is missing
        or dont exist'''
        commands = arguments.split()
        if len(commands) == 0:
            print("** class name missing **")
            return None

        elif commands[0] not in classes:
            print("** class doesn't exist **")
            return None

        elif mode == 1:
            if len(commands) < 2:
                print("** instance id missing **")
                return None

        return commands

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel'''
        commands = self.verification(arg, 0)

        if commands is None:
            return

        instance_name = commands[0]
        if instance_name == "BaseModel":
            new_instance = BaseModel()

        if instance_name == "User":
            new_instance = User()

        if instance_name == "State":
            new_instance = State()

        if instance_name == "City":
            new_instance = City()

        if instance_name == "Amenity":
            new_instance = Amenity()

        if instance_name == "Place":
            new_instance = Place()

        if instance_name == "Review":
            new_instance = Review()

        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.'''
        commands = self.verification(arg, 1)

        if commands is None:
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = storage.all()

        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            print(instances_dict[key])

    def do_destroy(self, arg):
        ''' Prints the string representation of an instance based on the class name
        and id. Ex: $ show BaseModel 1234-1234-1234.'''
        commands = self.verification(arg, 1)

        if commands is None:
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = storage.all()

        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            del instances_dict[key]
            storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all.'''
        classes_to_print = arg.split()
        instances_dict = storage.all()
        instances_list = []

        for cls in classes_to_print:
            if cls not in classes:
                print("** class doesn't exist **")
                return None

        for object in instances_dict.values():
            if len(classes_to_print) > 0:
                if object.to_dict()['__class__'] in classes_to_print:
                    instances_list.append(object.__str__())
            else:
                instances_list.append(object.__str__())

        print(instances_list)

    def do_update(self, arg):
        ''' Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file). Ex: $
        update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"'''
        commands = self.verification(arg, 1)
        if commands is None:
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = models.storage.all()

        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            if len(commands) < 3:
                print("** attribute name missing **")
                return

            if len(commands) < 4:
                print("** value missing **")
                return

            object_to_update = instances_dict[key]
            attribute = commands[2]
            new_value = commands[3]

            try:
                type_attribute = type(getattr(object_to_update, attribute))
                casted_value = cast_variable(new_value, type_attribute)
                setattr(object_to_update, attribute, casted_value)
            except:
                setattr(object_to_update, attribute, new_value)
            object_to_update.save()

    def do_BaseModel(self, line):
        '''Creating the Method to execute BaseModel'''
        arg = get_line(line)
        command = arg[0] + " BaseModel"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)

    def do_City(self, line):
        '''Creating the Method to execute City'''
        arg = get_line(line)
        command = arg[0] + " City"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)

    def do_Place(self, line):
        '''Creating the Method to execute Place'''
        arg = get_line(line)
        command = arg[0] + " Place"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)

    def do_Review(self, line):
        '''Creating the Method to execute Review'''
        arg = get_line(line)
        command = arg[0] + " Review"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)

    def do_State(self, line):
        '''Creating the Method to execute State'''
        arg = get_line(line)
        command = arg[0] + " State"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)

    def do_User(self, line):
        '''Creating the Method to execute User'''
        arg = get_line(line)
        command = arg[0] + " User"

        for i in range(1, len(arg)):
            command += " " + arg[i]
        self.onecmd(command)


def cast_variable(variable, new_type):
    '''Recognize the type of the varible to be change i the update function'''
    if new_type == int:
        return int(variable)

    elif new_type == float:
        return float(variable)

    elif new_type == list:
        return list(variable)

    elif new_type == dict:
        return dict(variable)

    return variable


def get_line(line):
    '''Creating the argumments for the specific class methods'''

    change_line = ""
    characters = ["\"", "(", ")", ".", ",", "}", "{", ":"]

    for char in line:
        if char in characters:
            change_line += " "

        else:
            change_line += char

    argumments = change_line.split()

    return argumments

if __name__ == '__main__':
    HBNBCommand().cmdloop()
