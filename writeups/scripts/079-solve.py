from pathlib import Path
import re

text = Path("sequence.txt").read_text()
positions = [1, 2, 3, 5, 8, 13, 21, 34]
prose = text.split("{", 1)[0]
sentences = [part.strip() for part in re.split(r"\.\s*", prose)
             if part.strip()]
first_word = "".join(sentences[i - 1][0] for i in positions
                     if i <= len(sentences))
json_text = text[text.index("{"):text.rindex("}") + 1]
keys = re.findall(r'^\s*"([^"\n]+)"\s*:', json_text, re.M)
second_word = "".join(keys[i - 1][0] for i in positions)
print(first_word, second_word)
