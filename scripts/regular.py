import re

def extract_pattern(text, pattern, verbose=False):
    if 'Subestación Afectada' in pattern:
        # Extract ALL IN patterns per substation
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
            
            for in_pattern in in_patterns:
                matches.append((substation, in_pattern.strip()))
    else:
        # Use regular findall for other patterns
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

def main():
    input_files = [
        'data/parsed/messages_data1.txt',
        'data/parsed/messages_data2.txt',
        'data/parsed/messages_data3.txt',
        'data/parsed/messages_data4.txt',
        'data/parsed/messages_data5.txt'
    ]
    
    patterns = {
        # 'IN_numbers': r'IN-[a-z0-9A-Z]+[^\n•]*',
        'Substations': r'(Subestación Afectada:)([^⚡]+)⚡.*IN-[a-z0-9A-Z]+[^\n•]*',
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