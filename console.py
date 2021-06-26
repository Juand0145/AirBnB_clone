#!/usr/bin/python3
''' '''
import cmd
import models
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel()}


class HBNBCommand(cmd.Cmd):
    ''' '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        ''' Quit program to exit the program'''
        if arg is not None:
            exit()

    def do_EOF(self, arg):
        ''' Quit program to exit the program '''
        if arg is not None:
            exit()

    def verification(self, arguments, mode):

        commands = arguments.split()
        if len(commands) == 0:
            print("** class name missing **")
            return None

        elif commands[0] not in classes.keys():
            print("** class doesn't exist **")
            return None

        elif mode == 1:
            if len(commands) < 2:
                print("** instance id missing **")
                return None

        return commands

    def do_create(self, arg):
        ''' '''
        commands = self.verification(arg, 0)

        if commands is None:
            return

        instance = classes[commands[0]]
        storage.new(instance)
        storage.save()
        print(instance.id)

    def do_show(self, arg):
        ''' '''
        commands = self.verification(arg, 1)

        if commands is None:
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = models.storage.all()

        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            print(instances_dict[key])

    def do_destroy(self, arg):
        ''' '''
        commands = self.verification(arg, 1)

        if commands is None:
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = models.storage.all()

        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            instances_dict.pop(key)
            models.storage.save()

    def do_all(self, arg):
        ''' '''
        classes_to_print = arg.split()
        instances_dict = models.storage.all()
        instances_list = []

        for cls in classes_to_print:
            if cls not in classes.keys():
                print("** class doesn't exist **")
                return None

        for object in instances_dict.values():
            if len(classes_to_print) > 0:
                for cls in classes.values():
                    if type(object) == type(cls):
                        instances_list.append(object.__str__())
            else:
                instances_list.append(object.__str__())

        print(instances_list)

    def do_update(self, arg):
        ''' '''
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
            casted_value = cast_variable(new_value, type(getattr(object_to_update, attribute)))
            setattr(object_to_update, attribute, casted_value)
            object_to_update.save()


def cast_variable(variable, new_type):
    ''' '''
    if new_type == int:
        return int(variable)

    elif new_type == float:
        return float(variable)

    elif new_type == list:
        return list(variable)

    elif new_type == dict:
        return dict(variable)

    return variable


if __name__ == '__main__':
    HBNBCommand().cmdloop()
