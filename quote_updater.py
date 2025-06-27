import random
import re

quotes = [
    "Simplicity is the soul of efficiency.",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Every bug is a lesson in disguise.",
    "In the middle of difficulty lies opportunity. – Einstein",
    "Sometimes you build out of need. Sometimes, out of envy."
]

new_quote = f'🧠 **Daily Thought:** *"{random.choice(quotes)}"*'

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace everything between <!--QUOTE_START--> and <!--QUOTE_END-->
new_content = re.sub(
    r'<!--QUOTE_START-->.*?<!--QUOTE_END-->',
    f'<!--QUOTE_START-->\n{new_quote}\n<!--QUOTE_END-->',
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)