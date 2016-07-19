"""
Entry point for the ascii_cat CLI
"""
import sys
import argparse
from ascii_cat import __version__
from ascii_cat import ascii_converter
from ascii_cat import get_cats


def cats_options(parser):
    """
    Add arguments to the cats command
    """
    parser.add_argument(
        '--breeds',
        help=(
            'List of cat breeds to search by. At least one must be '
            'specified if the parameter is chosen. Max 5.'),
        nargs='+')
    parser.add_argument(
        '--fluffy',
        help='Search for fluffy kitties',
        action='store_true')
    parser.add_argument(
        '--funny',
        help='Search for funny cat pictures',
        action='store_true')
    parser.add_argument(
        '--kitten',
        help='Search for kitten pictures',
        action='store_true')
    parser.add_argument(
        '--other',
        help=(
            'Another option to add to the query because I can\'t provide '
            'all the options we might want to search on. You can specify '
            '1 to 5 more query parameters here.'),
        nargs="+")

def meme_options(parser):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--grumpy',
        help='Grumpy Cat',
        action='store_true')
    group.add_argument(
        '--bubs',
        help='Bubs the Cat',
        action='store_true')
    group.add_argument(
        '--business_cat',
        help='Business Cat',
        action='store_true')
    group.add_argument(
        '--lolcats',
        help='LolCats: a.k.a. I Can Has Cheezburger',
        action='store_true')
    group.add_argument(
        '--nyan',
        help='Nyan Cat',
        action='store_true')
    group.add_argument(
        '--hipster',
        help='Hipster Cat',
        action='store_true')
    group.add_argument(
        '--longcat',
        help='Longcat',
        action='store_true')


def build_parser(args):
    parser = argparse.ArgumentParser(
        prog="ascii_cat",
        description="There is nothing better than cats on your command line")
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {}'.format(__version__))
    parser.add_argument(
        '-n', '--number',
        help=(
            'Choose the number of images to return. Options are 1 to 5. '
            'Default: 1'
        ),
        choices=range(1, 6),
        type=int,
        default=1)

    subparsers = parser.add_subparsers(title='Commands', dest='command')

    cats = subparsers.add_parser(
        'cats',
        help='Find pictures of cats in general')
    cats_options(cats)

    meme = subparsers.add_parser(
        'meme',
        help='Find cat memes'
    )
    meme_options(meme)

    random = subparsers.add_parser(
        'random',
        help='Get random cat pictures'
    )

    opts = parser.parse_args(args)

    if opts.command == 'cats':
        if opts.breeds and len(opts.breeds) > 5:
            cats.error(
                'Too many breeds specified! Max of 5 breeds allowed in query')
        if opts.other and len(opts.other) > 5:
            cats.error(
                'Too many additional query args! Max of 5 allowed!')

    return opts


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    opts = build_parser(argv)

    query = get_cats.construct_query(opts)
    search_results = get_cats.search(query=query)
    selection = get_cats.select_results(search_results, num_results=opts.number)

    for img_resp in selection:
        img = get_cats.get_image_content(img_resp['link'])
        if img is not None:
            print(ascii_converter.handle_image_conversion(img))

if __name__ == '__main__':
    main()
