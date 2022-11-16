# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#!/usr/bin/python

import sys
from modules.ScraperYT import Scraper
import os
import json


def main(argv):
    outdata= {}
    if len(argv)==4:
        if argv[0] == "--input"  and argv[2]=="--output" and os.path.isfile(argv[1]):
            input_file = argv[1]
            output_file = argv[3]
            with open(input_file, "r") as file:
                json_data = json.load(file)
                for id in json_data['videos_id']:
                    try:
                        scraper = Scraper(f"https://www.youtube.com/watch?v={id}")
                    except Exception as e:
                        print(e)
                    else:
                        result = scraper.get_all()
                    with open(output_file,"a") as outfile:
                        outfile.write(json.dumps(result))
        else:
            print("ERROR: Bad Input\nUsage: main.py --input <inputfile> --output <outputfile>")
    else:
        print("ERROR: Too few arguments\nUsage: main.py --input <inputfile> --output <outputfile>")

if __name__ == "__main__":
   main(sys.argv[1:])

# Press the green button in the gutter to run the script.





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
