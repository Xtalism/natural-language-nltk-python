# Natural Language Chat with NLTK and Python

A project to build a chat application using Natural Language Processing (NLP) with the Natural Language Toolkit (NLTK) and Gensim.

## 📋 Overview

This project focuses on creating a chat application that can understand and respond to user input in natural language. It utilizes NLTK for core NLP tasks and Gensim for handling word embeddings to better understand context and meaning.

## 🚀 Features

- **Natural Language Understanding**: Process and understand user input using NLTK.
- **Contextual Conversations**: Maintain context to provide relevant responses.
- **Word Embeddings**: Use Gensim and Word2Vec for semantic understanding.
- **Extensible Architecture**: Designed to be modular and easy to extend with new capabilities.

## 🛠️ Prerequisites

- Python 3.12.3 or higher
- Ubuntu 24.04 (or any Linux distribution)
- pip package manager

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd natural-language-nltk-python
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
# or
# venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
# Upgrade pip and install build tools
pip install -U nltk
pip install -U gensim
# or you can install requirements.txt
# pip install -r requirements.txt
```

### 4. Download NLTK Data

```bash
python3 -m nltk.downloader all
```

You can install it using nltk GUI downloader by running in python:
```python
import nltk
nltk.download()
```

## 🏃‍♂️ Usage

Run the main analysis script to see NLTK in action:
```bash
python3 main.py
```

Run the Gensim script to explore word embeddings:
```bash
python3 gensim_setup.py
```

## 📁 Project Structure

```
natural-language-nltk-python/
├── main.py          # Main NLTK analysis script
├── gensim_setup.py  # Gensim Word2Vec demonstration
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── LICENSE          # License file
```

## 🔍 Objectives

- **Build a Chat Application**: Create a functional chat application from scratch.
- **Implement NLU**: Use NLTK for tokenization, and other NLP tasks to understand text.
- **Leverage Word Embeddings**: Use Gensim to work with Word2Vec for better text comprehension.
- **Structure an NLP Project**: Organize code for a real-world NLP application.

## 📚 Resources

- [NLTK Documentation](https://www.nltk.org/)
- [Gensim Documentation](https://radimrehurek.com/gensim/)

## 📄 License

This project is licensed under the terms specified in the LICENSE file.