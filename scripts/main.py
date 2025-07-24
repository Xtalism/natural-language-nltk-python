import sys
from parser import parse_file as html_parse

from regular import parse_files as regex_extract

from data import data_files, patterns


class main:
    html_parse("data/messages.html", "data/parsed/messages_data1.txt")
    html_parse("data/messages2.html", "data/parsed/messages_data2.txt")
    html_parse("data/messages3.html", "data/parsed/messages_data3.txt")
    html_parse("data/messages4.html", "data/parsed/messages_data4.txt")
    html_parse("data/messages5.html", "data/parsed/messages_data5.txt")

    regex_extract(data_files, patterns)


if __name__ == "__main__":
    sys.exit(main())
