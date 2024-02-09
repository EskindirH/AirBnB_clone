#!/usr/bin/python3
"""
This module contains the entry point
of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel

class class HBNBCommand(cmd.Cmd):
    """Command interpreter implementing Cmd class"""
    prompt = "(hbnb "
    models = ['BaseModel']
    cmds = ['create', 'show', 'all', 'update', 'destroy', 'count']

    def do_quit(self, line):
        """Exits the interprater"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the interprater"""
        return True

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
