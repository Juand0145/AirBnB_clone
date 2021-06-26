#!/usr/bin/python3
''' '''
import cmd
import json
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

    def verification(self, arguments):

        commands = arguments.split()
        if len(commands) == 0:
            print("** class name missing **")
            return None

        elif commands[0] not in classes.keys():
            print("** class doesn't exist **")
            return None

        return commands

    def do_create(self, arg):
        ''' '''
        commands = self.verification(arg)

        if commands is not None:
            instance = classes[commands[0]]
            instance.save()
            print(instance.id)
    
    def do_show(self, arg):
        ''' '''
        commands = self.verification(arg)
        
        if commands is None:
            return

        if len(commands) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        instances_dict = models.storage.all()
        
        if key not in instances_dict.keys():
            print("** no instance found **")

        else:
            print(instances_dict[key])

    def do_destroy(self, arg):
        ''' '''
        commands = self.verification(arg)

        if commands is None:
            return

        if len(commands) < 2:
            print("** instance id missing **")
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
        commands = arg.split()
        instances_dict = models.storage.all()
        instances_list = []

        if commands not in classes.keys():
            print("** class doesn't exist **")
            return None
        
        for object in instances_dict.values():
            instances_list.append(object.__str__)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
