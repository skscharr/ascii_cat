"""
Entry point for the ascii_cat CLI
"""
import sys
import argparse
import get_cats


def cats_options(parser):
    """
    Add arguments to the cats command
    """
    parser.add_argument(
        '--breed',
        help=(
            'List of cat breeds to search by. At least one must be '
            'specified if the parameter is chosen. Max 5.'),
        nargs='+')
    parser.add_argument(
        '--color',
        help=(
            'Dominant color to search by. Available choices are black, blue, '
            'brown, gray, green, pink, purple, teal, white, and yellow. '
            'Select only 1'),
        choices=[
            "black", "blue", "brown", "gray", "green", "pink", "purple",
            "teal", "white", "yellow"])
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
    """
    Add arguments to the meme command. This command is grouped to
    restrict the options allowing the user to select only one, and
    one must be selected.
    """
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
        help='Search for images by popular cat memes')
    meme_options(meme)

    random = subparsers.add_parser(
        'random',
        help='Get random cat pictures'
    )

    opts = parser.parse_args(args)

    if opts.subcommand == 'cats' and (opts.breeds or opts.other):
        if len(opts.breeds) > 5:
            cats.error(
                'Too many breeds specified! Max of 5 breeds allowed in query')
        if len(opts.other) > 5:
            cats.error(
                'Too many additional query args! Max of 5 allowed!')

    return opts


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    opts = build_parser(argv)

    query = construct_query(opts)
    search_results = get_cats.search()



if __name__ == '__main__':
    main()
