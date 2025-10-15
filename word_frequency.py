#!/usr/bin/env python3

# Word frequency – Lab 3
# Prompts for a valid sentence, then prints frequencies using parallel lists.

import re

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

# 1) Prompt until a valid sentence (per helper)
user_sentence = input("Enter a sentence: ")
while not is_sentence(user_sentence):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# 2) Normalize to lowercase and split
raw_words = user_sentence.lower().split()

# 3) Clean punctuation (keep letters/numbers inside words)
cleaned = []
for w in raw_words:
    # remove leading/trailing punctuation like commas/quotes
    w = re.sub(r"^[^\w]+|[^\w]+$", "", w)
    if w:
        cleaned.append(w)

# 4) Build frequencies using two parallel lists (words & counts)
words = []
counts = []
for w in cleaned:
    try:
        i = words.index(w)
        counts[i] += 1
    except ValueError:
        words.append(w)
        counts.append(1)

# 5) Print results
for w, c in zip(words, counts):
    print(f"{w}: {c}")
