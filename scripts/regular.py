import re


class RegularParser:
    def __init__(self, data_files=None, patterns=None):
        self.data_files = data_files if data_files is not None else []
        self.patterns = patterns if patterns is not None else {}

    def add_file(self, file_path):
        self.data_files.append(file_path)

    def add_pattern(self, name, pattern):
        self.patterns[name] = pattern

    def extract_substations(self, text, pattern, verbose=False):
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if verbose:
            print(f'\nFound {len(matches)} matches for pattern "{pattern}":\n{matches}')
        return matches

    def extract_pattern(self, text, pattern, verbose=False):
        if "Subestación Afectada" in pattern:
            substation_blocks = re.finditer(
                r"Subestación Afectada:([^⚡]+)⚡([^📍]*)(?=📍|$)",
                text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            matches = []
            for block in substation_blocks:
                substation = block.group(1).strip()
                block_content = block.group(2)
                in_patterns = re.findall(
                    r"IN-[a-z0-9A-Z]+[^\n•]*", block_content, flags=re.IGNORECASE
                )
                pr_patterns = re.findall(
                    r"PR-[a-z0-9A-Z]+[^\n•]*", block_content, flags=re.IGNORECASE
                )
                for in_pattern in in_patterns:
                    matches.append((substation, in_pattern.strip()))
                for pr_pattern in pr_patterns:
                    matches.append((substation, pr_pattern.strip()))
        else:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if verbose:
            print(f'\nFound {len(matches)} matches for pattern "{pattern}":\n{matches}')
        return matches

    def open_file(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def save_file(self, messages, output_filename):
        with open(output_filename, "w") as file:
            for message in messages:
                if isinstance(message, tuple):
                    parts = [re.sub(r"\s+", " ", str(part)).strip() for part in message]
                    clean_message = " | ".join(parts)
                else:
                    clean_message = re.sub(r"\s+", " ", str(message)).strip()
                file.write(clean_message + "\n")

    def process_file(self):
        for i, filename in enumerate(self.data_files):
            content = self.open_file(filename)
            for pattern_name, pattern in self.patterns.items():
                extract = self.extract_pattern(content, pattern, True)
                extract_sub = self.extract_substations(content, pattern, True)
                if pattern_name == "Substations_all":
                    self.save_file(extract, f"data/extraction/data_all_{i + 1}.txt")
                elif pattern_name == "Substations_only":
                    self.save_file(
                        extract_sub, f"data/extraction/data_substations_{i + 1}.txt"
                    )
                elif pattern_name == "IN_numbers":
                    self.save_file(extract, f"data/extraction/data_in_{i + 1}.txt")
                elif pattern_name == "PR_numbers":
                    self.save_file(extract, f"data/extraction/data_pr_{i + 2}.txt")
                else:
                    self.save_file(extract, f"data/extraction/data_{i + 1}.txt")


def parse_files(data_files, patterns):
    parser = RegularParser(data_files, patterns)
    parser.process_file()
    print("Files processed according to provided patterns.")
