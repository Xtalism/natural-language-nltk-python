import re

def extract_pattern(text, pattern, verbose=False):
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    if verbose:
        print(f'\nFound {len(matches)} matches for pattern "{pattern}":\n{matches}')
    return matches

def open_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def save_file(messages, output_filename):
    with open(output_filename, 'w') as file:
        for message in messages:
            file.write(message + '\n')

text = open_file('examples/data/elon.txt')
document = open_file('examples/data/document.txt')
financial = open_file('examples/data/financial.txt')

text_pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}|\d{3}-\d{3}-\d{3}'
document_pattern = r'Note \d - ([^\n]*)'
financial_pattern = r'FY(\d{4} Q[1-4])'
financial_money_pattern = r'\$([0-9\.]+)'
mergerd_pattern = r'FY(\d{4} Q[1-4])[^\$]+\$([0-9\.]+)'
 
extract_pattern(document, document_pattern, True)
extract_pattern(text, text_pattern, True)
extract_pattern(financial, financial_pattern, True)
extract_pattern(financial, financial_money_pattern, True)
extract_pattern(financial, mergerd_pattern, True)

matches = re.search(mergerd_pattern, financial)
print(matches.groups())