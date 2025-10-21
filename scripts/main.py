from textwrap import wrap

read_file_path = input("Please input the file path here, it should look something like this: 'C:/Users/yourName/yourFolder/yourFile.txt' please note you MUST use forward slashes in your file path or else it will not work\n")
write_file_path = "output.txt"
final_content = ""

with open(read_file_path, 'r') as file: #Read the file and split it, using 75 "="s as a divider
    content = file.read()
    split_content = wrap(content, 256)
    for i in split_content:
        final_content += f"{i}\n"
        final_content += '=' * 75
        final_content += '\n'

with open(write_file_path, 'w') as file: #Write it to a new file, and confirm this to the user
    file.write(final_content)
    print(f"Your file has been succesfully split. You can find it under the name {write_file_path} in the minecraft-book-splitter folder!")
