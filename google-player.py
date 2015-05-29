#!./env/bin/python3

import sys
from subprocess import call
from queries.google_json_queries import get_google_results

def search(content, title):
    result = get_google_results("-inurl:(htm|html|php) intitle:”index of” +”last modified” +”parent directory” +description +size +(wma|mp3) “%s”" %content+" "+title, title)
    if len(result) < 3:
        return print("Fichier non trouvé :(")
    call(["vlc",result]) 
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : %s 'Artiste' 'Titre'" %sys.argv[0])
    else:
        search(sys.argv[1], sys.argv[2])
