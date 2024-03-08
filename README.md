Introducing the HBnB Console:

This project lays the foundation for an Airbnb clone by creating a console application. This interactive tool allows you to manage various objects within the platform, including Places, Cities, States, Amenities, Users, and Reviews. These objects inherit from a common base class called BaseModel.

Why a Console?

The console provides a stepping stone towards a full-fledged web application. It empowers you to interact with the system by creating, updating, displaying, counting, and deleting instances of these objects.

Getting Started

Execution: Open your terminal and navigate to the directory containing the console script. Then, run the following command:
Bash
./console.py
Use code with caution.
Help Command: Use the help command to explore available functionalities.

To list all commands: help
To get specific details about a command: help <command name>, for example, help quit
Creating Objects

Use the create command followed by the desired object class name (in PascalCase) to create a new object. Supported classes include:

BaseModel
User
Amenity
City
Place
State
Review
The created object's ID will be printed upon successful creation.

Viewing Objects

All Objects: Use all or <class_name>.all() to display all existing objects within a specific class or all classes if no class name is provided.

Specific Object: To view details of a particular object, use show <class_name> <id> or <class_name>.show("<id>"). For example, show Review 12345 or Review.show("12345").

Counting Objects

Use count <class_name> or <class_name>.count() to determine the number of objects belonging to a specific class (e.g., count Place or Review.count()).

Deleting Objects

To remove an object, use destroy <class_name> <id> or <class_name>.destroy("<id>"). For instance, destroy Review 12345 or Review.destroy("12345").

Updating Objects

The update command allows you to modify existing objects. There are three ways to achieve this:

update <class_name> <id> <attribute_name> "<new_value>": Updates a specific attribute with a new value. (e.g., update Review 12345 name "Marco")
<class_name>.update("<id>", "<attribute_name>", "<new_value>"): Similar to method 1, but using a class method. (e.g., City.update("12345", "item", "bed"))
<class_name>.update("<id>", {"<attribute_name1>": "<value1>", "<attribute_name2>": "<value2>"}): Updates multiple attributes simultaneously. (e.g., City.update("12345", {'item1': "bed", 'item2': "bathroom"}))
If the specified attribute already exists, it will be updated with the new value. Otherwise, a new attribute will be created for the object.

Exiting the Program

Use any of the following methods to exit the console:

Type quit
Press Ctrl+D
Reach the End-Of-File (EOF)
