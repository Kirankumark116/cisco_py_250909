import pickle 
flight={'flight_number':'1700','airline':'Indigo','capacity':225,'price':4500,'source':'banglore','destination':'Hyderabad'}
file_name='flight_dat'
print('Before file: ',flight)
with open(file_name,'wb') as writer:
    pickle.dump(flight,writer)
    print('saved the flight to file')

with open(file_name,'rb') as reader:
    flight_from_file=pickle.load(reader)
    print('Flight after read from file:', flight_from_file)