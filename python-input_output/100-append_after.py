def append_after(filename="", search_string="", new_string=""):
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return

    # Check if search_string is provided
    if not search_string:
        print("Please provide a search string.")
        return

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Open the file in write mode
    with open(filename, 'w') as file:
        # Iterate through the lines
        for line in lines:
            # Write the original line
            file.write(line)

            # Check if the search string is in the line
            if search_string in line:
                # If found, append the new string
                file.write(new_string + '\n')

# Example usage:
filename = "example.txt"
search_string = "specific string"
new_string = "This line is inserted after each line containing the specific string."

append_after(filename, search_string, new_string)

