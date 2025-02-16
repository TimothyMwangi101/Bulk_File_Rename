import os
import os.path

def getUserInput() -> None:
    """Prompts the user to enter the file path, extension and the new extention then passes those values to """
    path = input(r"Path: ") + "\\"
    ext = "." + input("Current Ext: ")
    extTo = "." + input("Change to: ")

    try:
        rename(path, ext, extTo)
    except Exception as e:
        print(f"You have a {type(e)}")
        print(e)

    return None

def rename(path, ext, extTo) -> None:
    """Changes the extension of each file to `extTO` and prints the result."""
    folder = os.listdir(path)
    for file in folder:

        if not file.endswith(ext):
            print (f"{file} =>\tNO CHANGE")
            continue
            
        newf = os.path.splitext(file)[0] + extTo
        os.rename(path + file, path + newf)
        print(f"{file} =>\t{newf}")

    return None
    
def main() -> None:
    """Main method of the Program"""
    getUserInput()
    return None

if __name__ == "__main__":
    main()