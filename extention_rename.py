import os
import os.path

def main() -> None:
    """Main method of the Program. Prompts the user to enter the file path, extension and the new extention"""
    path = input(r"Path: ") + "\\"
    ext = "." + input("Current Ext: ")
    extTo = "." + input("Change to: ")

    try:
        rename(path = path,ext = ext,extTo = extTo)
    except Exception as e:
        print(f"You have a {type(e)}")
        print(e)

    

def rename(path, ext, extTo) -> None:
    folder = os.listdir(path)
    for file in folder:

        if not file.endswith(ext):
            print (f"{file} => \tNO CHANGE \n")
            continue
            
        newf = os.path.splitext(file)[0] + extTo
        os.rename(path + file, path + newf)
        print(f"{file} => \t{newf} \n")
    
    
if __name__ == "__main__":
    main()