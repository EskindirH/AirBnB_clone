#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter implementing Cmd class.
    """
    prompt = "(hbnb) "
    mdls = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']
    cmds = ['create', 'show', 'all', 'update', 'destroy', 'count']

    def precmd(self, arg):
        """Parses command input

        Args:
            arg (str): input

        Returns:
            arg
        """
        if "." in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.mdls and cnd[0] in HBNBCommand.cmds:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """Prints help command description

        Returns:
            no return
        """
        print("Provides description of a given command")

    def empty_line(self):
        """Do nothing when empty line entered"""
        pass

    def do_count(self, cls_name):
        """Count number of instances of a class
        
        Args:
            cls_name: class name

        Returns:
            void
        """
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_create(self, model):
        """Creates instances of a class accordingly
        
        Args:
            model: any model class
        """

        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.mdls:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            mdl = dct[model]()
            print(mdl.id)
            mdl.save()

    def do_show(self, arg):
        """Prints the string representation of an instance

        Args:
            arg: string argument

        Returns:
            void
        """

        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(' ')
        if args[0] not in HBNBCommand.mdls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for k, v in all_objs.items():
                ob_name = v.__class__.__name__
                ob_id = v.id
                if ob_name == arg[0] and ob_id == arg[1].stip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance passed
        
        Args:
            arg: string argument
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.mdls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all 
        instances of a given class

        Args:
            arg: string arg

        Returns:
            void
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.mdls:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == args[0]:
                    list_instances += [value.__str__()]
            print(list_instances)

    def do_update(self, arg):
        """ Updates an instance based on 
        the class name and id.

        Args:
            arg: string argument
        """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.mdls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """Exits the interprater

        Args:
            line: command line

        Returns:
            True to exit
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the interprater

        Args:
            line: command line

        Returns:
            True to exit
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
