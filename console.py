#!/usr/bin/python3
''' '''
import cmd
import json
from models.base_model import BaseModel

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
        commands = self.verification(self, arg)

        if commands is not None:
            instance = classes[commands[0]]
            instance.save()
            print(instance.id)
    
    def do_show(self, arg):
        ''' '''
        commands = self.verification(self, arg)
        
        if len(commands) < 3:
            print("** instance id missing **")


    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
