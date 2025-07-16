import nltk, sys, parser
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.chat import chat, reflections

# 1. Configure NLTK to find your data
# nltk.data.path.append('/usr/share/nltk_data')  # Add system location
# print(f"NLTK data paths: {nltk.data.path}")

# 2. Verify punkt tokenizer is found

parser.HTMLParser.parse_file("data/messages.html", "data/messages_data1.txt")
parser.HTMLParser.parse_file("data/messages2.html", "data/messages_data2.txt")
parser.HTMLParser.parse_file("data/messages3.html", "data/messages_data3.txt")
parser.HTMLParser.parse_file("data/messages4.html", "data/messages_data4.txt")

class Main():
    def __init__(self):
        self.name = "main"
    try:
        punkt_path = nltk.data.find('tokenizers/punkt')
        print(f"Found punkt tokenizer at: {punkt_path}")
    except LookupError:
        print("Punkt tokenizer missing! Run: sudo python3 -m nltk.downloader -d /usr/share/nltk_data punkt")

    # 3. Test tokenization
    text = "Hello world! This is an NLTK test."
    tokens = word_tokenize(text)
    print(f"Tokenization test: {tokens}")

    # 4. Test corpus access
    try:
        print("\nFirst 10 words from Brown corpus:")
        print(brown.words()[:10])  # Should print: ['The', 'Fulton', 'County', 'Grand', ...]
    except Exception as e:
        print(f"Corpus access failed: {e}\nRun: sudo python3 -m nltk.downloader -d /usr/share/nltk_data brown")
    
if __name__ == '__main__':
    sys.exit(Main())