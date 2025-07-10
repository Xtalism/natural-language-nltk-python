import parser, sys
from bs4 import BeautifulSoup

with open("data/messages.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

messages = []
for div in soup.find_all("div", class_=lambda x: x and "message" in x.lower()):
    message_text = div.get_text(strip=True)
    if message_text:
        messages.append(message_text)

output_file = "messages_data.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for i, message in enumerate(messages, 1):
        f.write(f"Message {i}: {message}\n")

print(f"Extracted messages have been saved to {output_file}")
