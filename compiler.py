def compile_file(input_file_path):
    # Open input file
    with open(input_file_path, "r", -1, "utf-8") as input_file:
        # Read lines of input file
        lines = input_file.readlines()

    # An empty list to store the compiled code
    compiled_lines = []

    # Loop through all of the lines in the input file
    for line in lines:
        # Check if the line contains the word "say"
        if "напечатать" in line:
            # Replace "say" with "print"
            line = line.replace("напечатать", "print(")
            line = line.replace(".", ")")
        elif "переменная" in line:
            line = line.replace("переменная ", "")
            if "равна" in line:
                line = line.replace("равна", "=")
            line = line.replace(".", "")

        # Add the line to the list of compiled lines
        compiled_lines.append(line)

    code = "".join(compiled_lines)
    return code