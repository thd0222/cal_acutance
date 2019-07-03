import argparse

parser = argparse.ArgumentParser(description='Acutance calculator')

parser.add_argument('--src', type=str,
                    help='name or path of source images.')
parser.add_argument('--dst', type=str, default=None,
                    help='path of result data.')
parser.add_argument('--result', type=str,
                    help='name of result file.')

args = parser.parse_args()
