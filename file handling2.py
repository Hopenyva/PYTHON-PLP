with open("input.txt" , "r") as infile:
     content = infile.read()
     print(content)

modified_content = content.upper()

with open("output.txt" , "w") as outfile:
     outfile.write("===MODIFIED VERSION\n")
     outfile.write(modified_content)

print("File has been read and modified")


#ERROR HANDLING
def read_file():
     filename = input("Enter the filename: ")
     try:
          with open ("filename" , "r") as f:
               content = f.read()
               print("\n File content:\n")
               print(content)
     except FileNotFoundError:
          print(f"Error: The file '{filename}'was not found.")  

read_file()                  







          
               
               


