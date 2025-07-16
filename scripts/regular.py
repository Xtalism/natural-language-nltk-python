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

def main():
    input_files = [
        'data/messages_data1.txt',
        'data/messages_data2.txt',
        'data/messages_data3.txt',
        'data/messages_data4.txt'
    ]
    
    patterns = {
        'IN_numbers': r'IN-\d+',
        'PR_numbers': r'PR-\d+',
    }

    for i, filename in enumerate(input_files):
        content = open_file(filename)
        extract = extract_pattern(content, patterns['PR_numbers'], True)
        save_file(extract, f'data/extraction/cfe_extraction_{i+1}.txt')

main()