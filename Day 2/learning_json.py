import json
flight={'flight_number':'1700','airline':'Indigo','capacity':225,'price':4500,'source':'banglore','destination':'Hyderabad'}
file_name='flight_dat'
print('Before file: ',flight)
with open(file_name,'w') as writer:
    json.dump(flight,writer)
    print('saved the flight to file')

with open(file_name,'r') as reader:
    flight_from_file=json.load(reader)
    print('Flight after read from file:', flight_from_file)