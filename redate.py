import sys
import datetime
import re

def redate(lines):
    try:
        line_no = next(i for i, line in enumerate(lines)
                if line.startswith('\\lecture'))
        line = lines[line_no]
    except StopIteration:
        print(f'Error: no lecture found in file {sys.argv[1]}')
        sys.exit(1)
    match = re.search(r'\\lecture{(\d+)}{(.*?)}{(.*?)}', line)
    if match is None:
        match = re.search(r'\\lecture(\[\d+\])?{(.*?)}{(.*?)}', line)
        if match is None:
            print('Error: invalid lecture format')
            sys.exit(1)
        print('Already redated')
        return
    lec_no, date_str, title = match.groups()
    line = line.replace(f'{{{lec_no}}}', '')
    date = datetime.datetime.strptime(date_str, "%a %d %b '%y")
    new_date_str = date.strftime('%Y-%m-%d')
    line = line.replace(date_str, new_date_str)
    print(line)
    lines[line_no] = line

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: redate.py <filename>')
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r+') as lecture:
            lines = lecture.readlines()
            redate(lines)
            lecture.seek(0)
            lecture.writelines(lines)
            lecture.truncate()
    except FileNotFoundError:
        print(f'Error: {sys.argv[1]} not found')
        sys.exit(1)
