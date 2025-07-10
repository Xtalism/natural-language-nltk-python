from textblob import TextBlob

# wiki = TextBlob("Python is a high-level, general-purpose programming language.")
# print(wiki.tags)
# print(wiki.noun_phrases)

# testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
# print(testimonial.sentiment)

zen = TextBlob(
    "Beautiful is better than ugly. "
    "Explicit is better than implicit. "
    "Simple is better than complex. "
)
print(f"\nThese are your words:\n\n{zen.words}")
print(f"\nThese are your sentences:\n\n {zen.sentences}")


for sentence in zen.sentences:
    print(sentence.sentiment)