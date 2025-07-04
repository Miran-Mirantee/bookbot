from stats import report_chars
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    report_chars(sys.argv[1])
    
main()