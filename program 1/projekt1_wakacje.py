import csv

def write_to_file():
    with open("\cyber_studia\\vsc\hubertiwan\program 1\wydatki.csv", "a", newline = "") as wydatki_file:
        #we create an object to write to the file
        wydatki_write = csv.writer(wydatki_file)
        description = input("Enter the description of the expense: ")
        cost = int(input("Enter the cost of the expense: "))
        wydatki_write.writerow([description, cost])
        print("The expense has been added to the file.")

def read_from_file():
    with open("\cyber_studia\\vsc\hubertiwan\program 1\wydatki.csv", "r") as wydatki_file:
        #we create an object to read the file
        wydatki_read = csv.reader(wydatki_file)
        for row in wydatki_read:
            print(row[0] + " - " + row[1] + " PLN")
                
def delete_from_file():
    # Prompt the user to enter the row number to delete
    row_number = int(input("Enter the row number to delete: "))

    # Read the contents of the file
    with open("/cyber_studia/vsc/hubertiwan/program 1/wydatki.csv", "r") as wydatki_file:
        rows = list(csv.reader(wydatki_file))

    # Check if the row number is valid
    if row_number < 1 or row_number > len(rows):
        print("Invalid row number.")
        return

    # Remove the selected row from the list
    deleted_row = rows.pop(row_number - 1)

    # Write the updated contents back to the file
    with open("/cyber_studia/vsc/hubertiwan/program 1/wydatki.csv", "w", newline="") as wydatki_file:
        writer = csv.writer(wydatki_file)
        writer.writerows(rows)

    print("Row", row_number, "has been deleted:", deleted_row)
    
while(True):
    #decide whether you want to read a file or to write something to a file
    write_or_read = int(input("Do you want to read or to write something to a file? (1 - write, 2 - read, 3 - exit): "))

    if write_or_read == 1:
        write_to_file()
    elif write_or_read == 2:
        read_from_file()
    elif write_or_read == 3:
        delete_from_file()            
    elif write_or_read == 4: # exit the program
        break
    else:
        print("Invalid choice. Please enter 1 to write or 2 to read.")


    
    
    
    
    
    
    

