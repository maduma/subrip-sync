
import argparse

def main():
    parser = argparse.ArgumentParser(description='Sync SubRip subtitle with audio')
    parser.add_argument('filename', help='SubRip subtitle file (.srt). UFT-8 encoding')
    parser.add_argument('lag', help='lag in milliseconds. eg: 220, -150, +350')
    parser.add_argument('--no-backup', help='do not create a backup file (.bak)', action='store_true')
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
