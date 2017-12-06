import csv
import os

infile = raw_input("\nEnter the input filename\n")
# outputfile = raw_input("\nEnter the output filename\n")
searchwords = raw_input("\nEnter the words you need to search seperated by spaces\n")
str_arr = searchwords.split(' ')
arr = list()
for word1 in str_arr:
    arr.append(word1)

def contains_word(string, word):
    return (' ' + word + ' ') in (' ' + string + ' ')

def write_csv(inputfile, outputfile, searchword2):
    with open (inputfile, 'r') as csvfile:
        columns = csv.reader(csvfile)
        with open (outputfile, 'wb') as outfile:
            writer = csv.writer(outfile)
            for column in columns:
                text = column[3]
                # if not (contains_word(text, searchword2)):
                #     writer.writerow(column)
                if not searchword2 in text:
                    writer.writerow(column)

outfiles = list()
for searchword in arr:
    filname = searchword+'.csv'
    outfiles.append(filname)

write_csv(infile, outfiles[0], arr[0])
i1= len(outfiles)-1
i2= len(outfiles)-2
for i in range(0,i2):
    write_csv(outfiles[i], outfiles[i+1], arr[i+1])

write_csv(outfiles[i2], 'demofinal.csv', arr[i2])

for i in range(0,i1):
    os.remove(outfiles[i])

# write_csv(infile, 'final2.csv', 'u0')










        