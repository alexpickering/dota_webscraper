from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser()
    parser.add_argument('--items', choices=['one', 'two', 'three'])
    args = parser.parse_args()


if __name__ == '__main__':
    main()
