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
            clean_message = re.sub(r'\s+', ' ', message).strip()
            file.write(clean_message + '\n')

def main():
    input_files = [
        'data/messages_data1.txt',
        'data/messages_data2.txt',
        'data/messages_data3.txt',
        'data/messages_data4.txt'
    ]
    
    patterns = {
        'IN_numbers': r'IN-\d+[^\n•]*',
        'PR_numbers': r'PR-[a-z0-9A-Z]+[^\n•]*',
    }

    for i, filename in enumerate(input_files):
        content = open_file(filename)
        data =[]
        for _, pattern in patterns.items():
            extract = extract_pattern(content, pattern, True)
            data.extend(extract)
        save_file(data, f'data/extraction/data_ex_{i+1}.txt')

main()