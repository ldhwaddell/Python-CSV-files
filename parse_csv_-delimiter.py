import csv

#open original file to be read
with open("names.csv", "r") as csv_file:
    #use csv.reader method to read contents of file
    csv_reader = csv.reader(csv_file)

    #can be used to skip over first line
    #next(csv_reader)

    #opening a new file for writing
    with open("new_names.csv", "w") as new_file:
        #using writer method to write to new file with - as delimiter
        csv_writer = csv.writer(new_file, delimiter="-")

        #for each line in the original file, write out line into new file
        for line in csv_reader:
            csv_writer.writerow(line)



