def remove_comments(input_file, output_file):
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                if not line.strip().startswith('#'):
                    outfile.write(line)

input_file = 'your_python_code.py'
output_file = 'code_without_comments.py'
remove_comments(input_file, output_file)
