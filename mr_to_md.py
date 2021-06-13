import ntpath
import re
import sys


def main():
    try:
        path = None
        if len(sys.argv) == 2:
            path = sys.argv[1]
        elif len(sys.argv) > 2:
            print("Too many arguments!")
            exit(-1)
        else:
            path = input("Enter the path to the file: ")

        with open(path, 'r') as f:
            text = f.read().strip()

        print("Starting text\n", text, "\n------------------------------\n")
        md = text.replace("◆", "##").replace("\n \n", "\n").replace("\n───────────────\n", "\n")
        md = "# " + re.sub("[▪•]", "*", md)
        # remove "(Highlight: 170; Note: 1)" thing
        md.replace(md[md.find("("):-md.find(")")], "")
        filename, file_extension = ntpath.splitext(path)
        if file_extension.strip():
            newpath = path.replace(file_extension, f".md")
        else:
            newpath = path + ".md"

        print(f"File will be saved as {newpath}")
        with open(newpath, 'w') as f:
            f.write(md)
        print("Success")

    except Exception as e:
        print("Error: \n", e)


if __name__ == '__main__':
    main()
