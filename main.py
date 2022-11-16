# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#!/usr/bin/python

import sys
from Scraper import Scraper
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
                        print(f"https://www.youtube.com/watch?v={id}")
                        scraper = Scraper(f"https://www.youtube.com/watch?v={id}")
                    except:
                        print(f"Unable to obtain data from this video{id}")
                    else:
                        outdata[id] = scraper.get_all()
                        print(outdata)
                        with open(output_file,"a") as outfile:
                            outfile.write(json.dumps(outdata))
        else:
            raise Exception("ERROR: Bad Input\nUsage: main.py --input <inputfile> --output <outputfile>")
    else:
        raise Exception("ERROR: Too few arguments\nUsage: main.py --input <inputfile> --output <outputfile>")


if __name__ == "__main__":
   main(sys.argv[1:])

# Press the green button in the gutter to run the script.





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
