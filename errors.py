
def read_and_modify_file():
    # ask the user to input the file name
    input_filename = input ("Enter the file you want to read")
    
    # read the file 
    try: 
        with open (input_filename,"r") as file:
            content = file.readlines()
            print (content)
    
        #modify the file by numbering the lines
        modified_content = [f"{i+1}:{line}" for i, line in enumerate(content)]

        #ask the user for the file the want to write
        output_filename = input("Enter the file you want to write")

        with open(output_filename,"w") as file2:
            file2.write(modified_content)

    except FileExistsError:
        print("File doesn't exist, check the file name")
    except PermissionError:
        print("File cannot be accessed")

read_and_modify_file()