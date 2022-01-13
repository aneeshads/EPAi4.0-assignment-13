# Session 13 assignment of EPAi4.0
### Submitted by Aneesha Das
### E-mail id: dasaneesha@gmail.com

### Link to Deepnote notebook containing the logs of the programs written in the current assignment is as follows: 
https://deepnote.com/project/Starter-Project-z2QCsM9YTo-n6EzY4L3c-A/%2FEPAi4.0-session-13.ipynb

# Lazy Iterators

As discussed earlier, iterators are classes that contain both ‘iter’ and ‘next’ functions that enable an iterable to be iterable. Every time, the iteration is performed throughout the length of the iterable. However, lazy iterables. calculates the value only when the iteration happens as opposed to pre-calculating the value, and just fetching it during the iteration

# Generators and Iteration Tools I

Generators are iterators that are lazy in nature - whenever we execute a generator, it returns the generator object, and the execution of the code happens only when next() is called on the iterator. Generators are characterized by the presence of the 'yield' function.

## Brief description of the assignment
 
The file, nyc_parking_tickets_extract-1.csv, was provided which contained the following fields – Summons Number, Plate ID, Registration State, Plate Type, Issue Date, Violation code, Vehicle Body type, Vehicle Make and Violation Description. The assignment was broken down into two goals:
 
Goal 1: To create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, then the data has to be stored in a named tuple, and if the field is an integer, then it should be stored as an integer, etc.

Goal 2: To calculate the number of violations by car make.

## Description of functions implemented for solving Goal 1

### cast

The function cast has been written to convert each value to the appropriate data types. The Issue Date has been converted to a list, which will be further converted to a namedtuple; Summons Number and Violation code values have been converted to type integer. Plate ID, Registration State, Plate Type,  Vehicle Body type, Vehicle Make and Violation Description have been converted to string  type of data.

#### Usage:
cast(data_type, value)
where, data_type = datatype that the input value has to be converted to, </br>
	value = the parameter that has to be converted.

### cast_row

This function ‘cast_row’ has been written to convert the input data from a single row, which are all of string type, to the type corresponding to what has been assigned to them within the previous function.

#### Usage:

cast_row(data_types, data_row)

where, data_types = declared datatypes for each column in the file, </br>
	data_row = the row for which the data is being fetched.

### file_line_gen

This function defines the lazy iterator that returns the data of each row only when 'next' function is called. The presence of the 'yield' function signifies that the function is a generator.

## Description of functions implemented for solving Goal 2

The variable 'f1' is used to initiate the ‘file_line_gen’ function. However, since the function is a generator, the data rows will be displayed only when prompted. A for-loop has been assigned to iterate throughout the length of the file and display the data from the file.

