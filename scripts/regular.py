import re

data_files = [
    'data/parsed/messages_data1.txt',
    'data/parsed/messages_data2.txt',
    'data/parsed/messages_data3.txt',
    'data/parsed/messages_data4.txt',
    'data/parsed/messages_data5.txt'
]

patterns = {
    'Substations_all': r'(Subestación Afectada:)([^⚡]+)⚡.*(?:IN-|PR-)[a-z0-9A-Z]+[^\n•]*',
    'IN_numbers': r'IN-[a-z0-9A-Z]+[^\n•]*',
    'Substations_only': r'Subestación Afectada:([^⚡]+)⚡.*IN-[a-z0-9A-Z]+[^\n•]*',
    'PR_numbers': r'PR-[a-z0-9A-Z]+[^\n•]*',
}

def extract_substations(text, pattern, verbose=False):
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    if verbose:
        print(f'\nFound {len(matches)} matches for pattern "{pattern}":\n{matches}')
    return matches

def extract_pattern(text, pattern, verbose=False):
    if 'Subestación Afectada' in pattern:
        substation_blocks = re.finditer(
            r'Subestación Afectada:([^⚡]+)⚡([^📍]*)(?=📍|$)', 
            text, 
            flags=re.IGNORECASE | re.DOTALL
        )
        
        matches = []
        for block in substation_blocks:
            substation = block.group(1).strip()
            block_content = block.group(2)
            in_patterns = re.findall(r'IN-[a-z0-9A-Z]+[^\n•]*', block_content, flags=re.IGNORECASE)
            pr_patterns = re.findall(r'PR-[a-z0-9A-Z]+[^\n•]*', block_content, flags=re.IGNORECASE)
                        
            for in_pattern in in_patterns:
                matches.append((substation, in_pattern.strip()))
                
            for pr_pattern in pr_patterns:
                matches.append((substation, pr_pattern.strip()))
    else:
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
            if isinstance(message, tuple):
                parts = [re.sub(r'\s+', ' ', str(part)).strip() for part in message]
                clean_message = ' | '.join(parts)
            else:
                clean_message = re.sub(r'\s+', ' ', str(message)).strip()
            file.write(clean_message + '\n')

def process_file(input_files, pattern_dictionary):
        for i, filename in enumerate(input_files):
            content = open_file(filename)

            for pattern_name, pattern in pattern_dictionary.items():
                extract = extract_pattern(content, pattern, True)
                extract_sub = extract_substations(content, pattern, True)

                if pattern_name == 'Substations_all':
                    save_file(extract, f'data/extraction/data_all_{i+1}.txt')
                elif pattern_name == 'Substations_only':
                    save_file(extract_sub, f'data/extraction/data_substations_{i+1}.txt')
                elif pattern_name == 'IN_numbers':
                    save_file(extract, f'data/extraction/data_in_{i+1}.txt')
                elif pattern_name == 'PR_numbers':
                    save_file(extract, f'data/extraction/data_pr_{i+1}.txt')
                else:
                    save_file(extract, f'data/extraction/data_{i+1}.txt')

def main():
    process_file(data_files, patterns)
    # process_file(data_files, {'PR_numbers': patterns['PR_numbers']})
    # process_file(data_files, {'IN_numbers': patterns['IN_numbers']})
    # process_file(data_files, {'Substations': patterns['Substations']})
    print("Extraction completed successfully.")
    
main()