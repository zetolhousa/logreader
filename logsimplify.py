#!/usr/bin/env python3
import argparse

def filtering(iput):
    with open(iput) as f:
        for l in f:
            x = l.split()
            if '*' in x:
                continue
            else:
                print(l)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('iput', help="path of the log file")
    args = parser.parse_args()

    path = args.iput
    filtering(path)
    
if __name__ == '__main__':
    main()
