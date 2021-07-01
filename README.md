# 0x00. AirBnB clone - The console
The AirBnB project is one of the jewels crown in the Holberton academic pensum, This first approach we made a user interface from which we can create, modify and delete in our file storage.  You probably are asking yourself why would I do that? but this is a tool to interiorize the knowledge and comprehend what does and doesn't work in storage before to keep developing any web application.
![Logo Airbnb PNG transparente - StickPNG](http://assets.stickpng.com/images/580b57fcd9996e24bc43c513.png)

Airbnb is a company that offers a digital platform dedicated to the offer of accommodation to individuals and tourists (vacation rentals) through which hosts can advertise and hire the rental of their properties with their guests. Hosts and guests can rate each other as a reference for future users.

## Overview
Like any other user interface, our console works running a list of commands to execute a specific action that could be related to the creation, update, or deletion from a given instance inside our program. These instances belong to classes listed below:
 - BaseModel
 - User
 - State
 - City
 - Amenity
 - Place 
- Review

BaseModel is a class that defines all common attributes/methods for other classes, To improve the comprehension of how this inheritance model works, follow the next UML diagram.
![enter image description here](https://github.com/Juand0145/AirBnB_clone/blob/main/Untitled%20Diagram.png?raw=true)

## How to Start the console
The first step is to clone the repository using the following command:

    $ git clone https://github.com/Juand0145/AirBnB_clone.git
   Now to execute the console in interactive mode just enter to the repository and executed using the command:  

    $./console.py
   If everything works properly you should see a prompt (hbnb) and be able to write your commands there. If you want to acces in not interactive mode use the following command:

    echo "<command>" | ./console.py

## How to used it and examples
Next, I will present you a list of the commands that the console is allowed to interpreter and what are they supposed to do.

 - `EOF`: It is the acronym for End of file and will exit the console
 - `quit`: Exit the console
 - `<emptyline>`: overwrites default emptyline method and does nothing 
 - `create`: Creates a new instance using the classes presented in the overview section and saves it (to the JSON file) and prints the id
```
juand0145@DESKTOP-HTDB37B:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
d2393706-55e1-47ca-b86f-83faea4cc60e
(hbnb) create User
5119a616-6a57-4a64-9d76-1745058a54bb
(hbnb) create Place
828d63e0-35ee-4c8e-b45d-1f3a18b25e8c
(hbnb) create castle
** class doesn't exist **
(hbnb) 
```
 - `destroy`: Delete an instance based on the class name and id (save the change into the JSON file).
 ```
(hbnb) destroy BaseModel d2393706-55e1-47ca-b86f-83faea4cc60e
(hbnb) destroy User 5119a616-6a57-4a64-9d76-1745058a54bb
(hbnb) destroy castle 828d63e0-35ee-4c8e-b45d-1f3a18b25e8c
** class doesn't exist **
(hbnb) 
```
 - `show`: Prints the string representation of an instance based on the class name and id.
  ```
(hbnb) create BaseModel
602a36fe-9bff-4442-ac02-e451f6e7685e
(hbnb) show BaseModel 602a36fe-9bff-4442-ac02-e451f6e7685e
[BaseModel] (602a36fe-9bff-4442-ac02-e451f6e7685e) {'id': '602a36fe-9bff-4442-ac02-e451f6e7685e', 'created_at': datetime.datetime(2021, 6, 30, 13, 17, 56, 85719), 'updated_at': datetime.datetime(2021, 6, 30, 13, 17, 56, 85719)}
(hbnb) destroy BaseModel 602a36fe-9bff-4442-ac02-e451f6e7685e
(hbnb) show BaseModel 602a36fe-9bff-4442-ac02-e451f6e7685e
** no instance found **
(hbnb) 
 
```
 - `all`: Prints all string representation of all instances based on the class name or is empty print all instances previusly saved.
 ```
(hbnb) all
["[User] (abead54c-c971-4f2a-a36a-5499137a7fb8) {'id': 'abead54c-c971-4f2a-a36a-5499137a7fb8', 'created_at': '2021-06-30T13:09:01.415673', 'updated_at': '2021-06-30T13:09:01.415673', '__class__': 'User'}", "[BaseModel] (f726cacb-3f8d-4bb1-b4d8-06158a7e21d0) {'id': 'f726cacb-3f8d-4bb1-b4d8-06158a7e21d0', 'created_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451), 'updated_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451)}", "[BaseModel] (d7b166fe-f669-4d76-b333-b258b0303b30) {'id': 'd7b166fe-f669-4d76-b333-b258b0303b30', 'created_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329), 'updated_at': datetime.datetime
(hbnb) all
["[User] (abead54c-c971-4f2a-a36a-5499137a7fb8) {'id': 'abead54c-c971-4f2a-a36a-5499137a7fb8', 'created_at': '2021-06-30T13:09:01.415673', 'updated_at': '2021-06-30T13:09:01.415673', '__class__': 'User'}", "[BaseModel] (f726cacb-3f8d-4bb1-b4d8-06158a7e21d0) {'id': 'f726cacb-3f8d-4bb1-b4d8-06158a7e21d0', 'created_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451), 'updated_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451)}", "[BaseModel] (d7b166fe-f669-4d76-b333-b258b0303b30) {'id': 'd7b166fe-f669-4d76-b333-b258b0303b30', 'created_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329), 'updated_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329)}", "[User] (a6c61e35-81a8-4bb7-91ae-2c93ca2a8a53) {'id': 'a6c61e35-81a8-4bb7-91ae-2c93ca2a8a53', 'created_at': '2021-06-30T13:10:11.175846', 'updated_at': '2021-06-30T13:10:11.175846', '__class__': 'User'}", "[Place] (4d8e3c12-7aa7-4e30-ae71-e20baf739bf6) {'id': '4d8e3c12-7aa7-4e30-ae71-e20baf739bf6', 'created_at': '2021-06-30T13:10:14.152977', 'updated_at': '2021-06-30T13:10:14.152977', '__class__': 'Place'}", "[Place] (828d63e0-35ee-4c8e-b45d-1f3a18b25e8c) {'id': '828d63e0-35ee-4c8e-b45d-1f3a18b25e8c', 'created_at': '2021-06-30T13:15:25.255271', 'updated_at': '2021-06-30T13:15:25.255271', '__class__': 'Place'}"]
(hbnb) all Place
["[Place] (4d8e3c12-7aa7-4e30-ae71-e20baf739bf6) {'id': '4d8e3c12-7aa7-4e30-ae71-e20baf739bf6', 'created_at': '2021-06-30T13:10:14.152977', 'updated_at': '2021-06-30T13:10:14.152977', '__class__': 'Place'}", "[Place] (828d63e0-35ee-4c8e-b45d-1f3a18b25e8c) {'id': '828d63e0-35ee-4c8e-b45d-1f3a18b25e8c', 'created_at': '2021-06-30T13:15:25.255271', 'updated_at': '2021-06-30T13:15:25.255271', '__class__': 'Place'}"]
(hbnb) all Place BaseModel
["[BaseModel] (f726cacb-3f8d-4bb1-b4d8-06158a7e21d0) {'id': 'f726cacb-3f8d-4bb1-b4d8-06158a7e21d0', 'created_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451), 'updated_at': datetime.datetime(2021, 6, 30, 13, 9, 9, 480451)}", "[BaseModel] (d7b166fe-f669-4d76-b333-b258b0303b30) {'id': 'd7b166fe-f669-4d76-b333-b258b0303b30', 'created_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329), 'updated_at': datetime.datetime(2021, 6, 30, 13, 10, 4, 168329)}", "[Place] (4d8e3c12-7aa7-4e30-ae71-e20baf739bf6) {'id': '4d8e3c12-7aa7-4e30-ae71-e20baf739bf6', 'created_at': '2021-06-30T13:10:14.152977', 'updated_at': '2021-06-30T13:10:14.152977', '__class__': 'Place'}", "[Place] (828d63e0-35ee-4c8e-b45d-1f3a18b25e8c) {'id': '828d63e0-35ee-4c8e-b45d-1f3a18b25e8c', 'created_at': '2021-06-30T13:15:25.255271', 'updated_at': '2021-06-30T13:15:25.255271', '__class__': 'Place'}"]
(hbnb) all castle
** class doesn't exist **
(hbnb) 
```
 - `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
 ```
hbnb) create BaseModel
6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a
(hbnb) all
["[BaseModel] (6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a) {'id': '6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a', 'created_at': datetime.datetime(2021, 6, 30, 13, 24, 10, 879556), 'updated_at': datetime.datetime(2021, 6, 30, 13, 24, 10, 879556)}"]
(hbnb) update BaseModel 6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a first_name "Juan"
(hbnb) all
['[BaseModel] (6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a) {\'id\': \'6d3fdd3f-cbd9-4086-a7c0-771d57b4b81a\', \'created_at\': datetime.datetime(2021, 6, 30, 13, 24, 10, 879556), \'updated_at\': datetime.datetime(2021, 6, 30, 13, 24, 55, 392339), \'first_name\': \'"Juan"\'}']
(hbnb) 
```