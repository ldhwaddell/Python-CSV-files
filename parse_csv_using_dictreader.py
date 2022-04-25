import csv

# open original file to be read
with open("names.csv", "r") as csv_file:
    # use csv.reader method to read contents of file
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    # print(line["email"])

    # opening a new file for writing
    with open("new_names.csv", "w") as new_file:
        # create list of field names 
        fieldnames = ["first_name", "last_name", "email"]
        
        # using DictWriter method to write to new file with tab as delimiter
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames ,delimiter="\t")

        csv_writer.writeheader()

        # for each line in the original file, write out line into new file
        for line in csv_reader:
            csv_writer.writerow(line)
