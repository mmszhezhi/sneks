from snek import example
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name",type=str,default="call")
parser.add_argument("--fuck",action="store_true",default=False)
args = parser.parse_args()


def start():
    print(args.name)
    print(args.fuck)
    example.fuck()