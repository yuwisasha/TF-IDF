from collections import Counter
from math import log

import aiofiles


async def calculate_tf_idf(filename: str) -> dict[str: dict[str: float]]:
    async with aiofiles.open(filename, "r") as file:
        text = await file.read()
        strings = text.lower().splitlines()
        words = text.split()

    words_counts = Counter(words)
    words_total = len(words)
    strings_total = len(strings)

    tf_idf = {}
    
    for word, count in words_counts.items():
        tf = round((count / words_total), 2)
        idf = round(log(strings_total / (sum(word in string for string in strings))), 2)
        tf_idf[word] = {"tf": tf, "idf": idf}

    return dict(sorted(tf_idf.items(), key=lambda x: x[1]["idf"], reverse=True)[:50])