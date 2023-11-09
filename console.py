#!/usr/bin/python3
'''contains the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel, storage 


class HBNBCommand(cmd.Cmd):
    '''Command interpreter class'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''EOF to exit the program\n'''
        return True

    def emptyline(self):
        '''What happens when pressing enter\n'''
        return False

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist *")
            return
        obj = globals()[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        ''' Prints the string representation of an instance based on
        the class name and id'''
        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist *")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key in storage.all().keys():
            if storage.all()[key].id == args[1]:
                print(storage.all()[key])
                return
        print('** no instance found **')

    def do_destroy(self, line):
        ''' Deletes an instance based on the class name and id'''

        args = line.split()
        if not args:
            print('** class name missing **')
            return
        if not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist *")
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        for key in storage.all().keys():
            if storage.all()[key].id == args[1]:
                del(storage.all()[key])
                storage.save()
                return
        print('** no instance found **')

    def do_all(self, line):
        '''Prints all string representation of all instances based or not
        on the class name'''

        args = line.split()
        if args and not (args[0] in globals() and callable(globals()[args[0]])):
            print("** class doesn't exist *")
            return
        print([str(obj) for obj in storage.all().values()])

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
