#!./env/bin/python3

import sys
from queries.google_json_queries import get_google_results

def search(content):
    result = get_google_results("-inurl:(htm|html|php) intitle:”index of” +”last modified” +”parent directory” +description +size +(wma|mp3) “%s”" %content, content)
    print(result)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : %s 'query'" %sys.argv[0])
    else:
        search(sys.argv[1])
