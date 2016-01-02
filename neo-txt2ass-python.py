import argparse
import json

if __name__ == "__main__":
    desc = """Neo TXT2ASS Python. Generate ASS (Advanced Sub-Station Alpha) subtitle from JSON documents.

To generate a JSON, please use the web page attached.

Documentation: https://github.com/blueset/neo-txt2ass-python"""

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--input", "-i", type=argparse.FileType('r'), required=True, help="Input file (JSON)")
    parser.add_argument("--output", "-o", type=argparse.FileType('w'), help="Output file (JSON)")

    args = parser.parse_args()

    source = json.load(args.input)

    print(source)
