import argparse
from spacy.cli import download

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='Actions to execute')
    my_parser.add_argument('Action',
                       metavar='action',
                       type=str,
                       help='Action to execute with infinitive_clause.cli')
    args = my_parser.parse_args()
    
    if args.Action == "post_install": 
        download('en_core_web_trf')