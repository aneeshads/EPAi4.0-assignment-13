from collections import namedtuple

data_type = ['INT', 'STRING', 'STRING', 'STRING','DATE', 'INT', 'STRING','STRING', 'STRING']
file_name = 'nyc_parking_tickets_extract-1.csv'

def cast(data_type, value):
  """The function cast has been written to convert the appropriate types to each \
  field of data present within the file. The Issue Date has been converted to a list, \
  which will be further converted to a namedtuple; Summons Number and Violation code \
  values have been converted to type integer.Plate ID, Registration State, Plate Type, \
  Vehicle Body type, Vehicle Make and Violation Description have been converted to string \
  type of data.
  """
  if data_type == 'DATE':
    date = value.split('/')
    return date
  elif data_type == 'INT':
    return int(value)
  else:
    return str(value)

def cast_row(data_types, data_row):
  """This function cast_row has been written to convert the input data, which are \
  all of string type, to the type corresponding to what has been assigned to them \
  within the previous function.
  """
  return [cast(data_type, value)
          for data_type, value in zip(data_types, data_row)]

def file_line_gen(file):
  """This function defines the lazy iterator that returns the data of each row \
  only when 'next' function is called. The presence of the 'yield' function signifies that the \
  function is a generator - which is a type of lazy iterator.
  """
  with open(file) as f:
    file_iter = iter(f)
    headers = next(file_iter).strip('\n').split(',')
    headers = [i.replace(" ", "") for i in headers]
    Parkingticket = namedtuple('Parkingticket', headers)
    Date = namedtuple('Date', 'Day Month Year')
    for line in file_iter:
      data = line.strip('\n').split(',')
      data = cast_row(data_type, data)
      parking_ticket = Parkingticket(*data)
      parking_ticket = parking_ticket._replace(IssueDate=Date(*data[4]))
      yield parking_ticket
      
f1 = file_line_gen(file_name)
"""The variable 'f1' is used to initiate the file_line_gen function. However, \
since the function is a generator, the data rows will be displayed only when \
prompted. A for-loop has been assigned to iterate throughout the length of the \
file and display the data from the file.
"""
for line in f1:
    print(line)
    

    
def get_violations_by_car_make():
    """This function has been written to calculate the number of violations that \
    cars from each Vehicle Body type have on record.
    """
    car_make_dict = {}
    f1 = file_line_gen(file_name)
    for line in f1:
        if line.VehicleMake not in car_make_dict:
            car_make_dict.__setitem__(line.VehicleMake, 1)
        else:
            car_make_dict[line.VehicleMake] = car_make_dict[line.VehicleMake] + 1
    return car_make_dict
  
print(get_violations_by_car_make())
