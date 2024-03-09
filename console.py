#!/usr/bin/python3

"""
Console Module.

This module provides a command-line interface to manage
databases. It enables the creation, modification,
and deletion of instances for various classes.
"""

import re
import shlex
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command processor class:

    This class extends the cmd.Cmd class to implement
    a command-line interface for managing instances
    of different classes.

    Attributes:
        prompt (str): The command prompt displayed to the user.
        allowed_classes (list): The list of allowed class names
        for instance creation and manipulation.
    """

    prompt = '(hbnb)'
    allowed_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """
        Quit command:

        Exits the program.

        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.
        """

        return True

    def do_EOF(self, line):
        """
        EOF Command:

        Exits the program.
        Args:
            line (str): The command line input.

        Returns:
            bool: True to exit the program.
        """

        return True

    def do_create(self, line):
        """
        CreatesCommand:

        Creates a new instance of a specified class
        (e.g., BaseModel) and prints its unique identifier.

        Args:
            line (str): The command line input.
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Show Command:

        Prints the string representation of an
        instance based on the class name and id.

        Args:
            line (str): The command line input.
        """

        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(command + '.' + arg)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, line):
        """
        Destroy Command:

        Deletes an instance based on the class name and id.
        """

        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            key = command + '.' + arg
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """
        All Commad:

        Prints all string representations of instances based
        on the class name.
        """
        command = self.parseline(line)[0]
        objs = models.storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update Command:

        Updates an instance based on the class name and id by adding or
        updating attributes.
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()

    def analyze_parameter_value(self, value):
        """
        Analyze Parameter Value:

        Checks a parameter value for an update and converts it if necessary.

        Args:
            value (str): The value to analyze.

        Returns:
            Union[int, float, str]: The converted value.
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value

    def get_objects(self, instance=''):
        """
        Get Objects:

        Gets the elements created by the console.

        Args:
            instance (str, optional): The instance to find in the objects.

        Returns:
            list: If the instance argument is not empty, it will search
            only for objects that match the instance.
            Otherwise, it will show all instances in the file where all
            objects are stored.
        """
        objects = models.storage.all()

        if instance:
            keys = objects.keys()
            return [str(val) for key, val in objects.items()
                    if key.startswith(instance)]

        return [str(val) for key, val in objects.items()]

    def default(self, line):
        """
        Default Method:

        Handles unrecognized commands by looking for whether
        the command entered has the syntax:
        "<class name>.<method name>" and links it to
        the corresponding method if the class exists and the method
        belongs to the class.

        Args:
            line (str): The command line input.
        """
        if '.' in line:
            splitted = re.split(r'\.|\(|\)', line)
            class_name = splitted[0]
            method_name = splitted[1]

            if class_name in self.allowed_classes:
                if method_name == 'all':
                    print(self.get_objects(class_name))
                elif method_name == 'count':
                    print(len(self.get_objects(class_name)))
                elif method_name == 'show':
                    class_id = splitted[2][1:-1]
                    self.do_show(class_name + ' ' + class_id)
                elif method_name == 'destroy':
                    class_id = splitted[2][1:-1]
                    self.do_destroy(class_name + ' ' + class_id)

    def emptyline(self):
        """
        Empty Line Method:

        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.
        """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
