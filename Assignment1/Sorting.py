import sys

def sort_output():
    lines = sys.stdin.readlines()
    sorted_lines = sorted(line.strip() for line in lines)
    
    for line in sorted_lines:
        print(line)

if __name__ == "__main__":
    sort_output()
