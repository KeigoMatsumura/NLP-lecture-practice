import CaboCha
import sys

if __name__ == "__main__":
    cp = CaboCha.Parser()
    text = sys.argv[1]
    print(cp.parseToString(text))
