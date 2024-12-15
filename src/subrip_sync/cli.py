
import argparse

def main():
    parser = argparse.ArgumentParser(description='Sync SubRip subtitle with audio')
    parser.add_argument('filename', help='SubRip (.srt) subtitle file. UFT-8 encoding')
    parser.add_argument('lag', help='lag in milliseconds. eg: 220, -150, +350')
    parser.parse_args()


if __name__ == "__main__":
    main()
