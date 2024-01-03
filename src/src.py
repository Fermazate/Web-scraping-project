import argparse

from fetch import fetch_web

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str, help='URL to fetch')
args = parser.parse_args()

def main(*args):
    fetch_web(args.url)

if __name__ == '__main__':
    main()
