from bs4 import BeautifulSoup


class HTMLParser:
    def __init__(self, html_content=None):
        self.soup = BeautifulSoup(html_content, "html.parser") if html_content else None

    def open_file(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def get_messages(self):
        if not self.soup:
            raise ValueError("HTML content is not set.")
        return self.soup.find_all("div", class_=lambda x: x and "message" in x.lower())

    def save_file(messages, output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            for i, message in enumerate(messages, 1):
                f.write(f"Message {i}: {message}\n")


def parse_file(file_path, output_file):
    html_content = HTMLParser.open_file(file_path)
    parser = HTMLParser(html_content)
    messages = []
    for div in parser.get_messages():
        message_text = div.get_text(strip=True)
        if message_text:
            messages.append(message_text)
    HTMLParser.save_file(messages, output_file)
    print(f"Extracted messages have been saved to {output_file}")
