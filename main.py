import csv

filename = "funnyfile.csv"

fields = []
rows = []
pressures = []
temperatures = []

with open(filename,"r") as csvfile: 
  csvreader = csv.reader(csvfile)

  fields = next(csvreader)

  for row in csvreader:
    rows.append(row)

  print("Number of rows: %d"%(csvreader.line_num))

print('Fields :' + ', '.join(field for field in fields)) #general convention probably stupid    

#this might be because fields cant be auto used as iterators i cry i cry i cry

#UPDATE: alright so in the join function, you must declare field first, but for general interation you not only dont do that, but cant, i hate python make it stop plaease

pIndex = -1 #pressure index
tIndex = -1 #temprature index
for i in range(len(fields)):
    if fields[i] == "Pressure":
      pIndex = i
    elif fields[i] == "Temprature":
      tIndex = i


# get all pressure and temperature data
    for col in rows[pIndex]:
        print("%10s"%col),  #through python lamb sacrafice   we parse the collums
        val = "%10s"%col
        pressures.append(val) #hopefully lets us use the values as numbers and not strings
        print('\n')

    for col in rows[tIndex]:
        print("%10s"%col),
        val = "%10s"%col
        temperatures.append(val)
        print('\n')