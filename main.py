import sys
from stats import print_report
# sys.argv[0] = "main.py"
# sys.argv[1] = first argument after script name, in this case, the file path

# Check if the script is run with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1) # this will exit with error code 1

# Get the path to the book from the command line arguments
path_to_book = sys.argv[1]
try:
    with open(path_to_book) as f:
        print_report(path_to_book)
except FileNotFoundError:
    print(f"File not found: {path_to_book}")
    sys.exit(1)