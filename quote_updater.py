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

# Pattern match everything inside quote markers
pattern = r'<!--QUOTE_START-->.*?<!--QUOTE_END-->'
replacement = f'<!--QUOTE_START-->\n{new_quote}\n<!--QUOTE_END-->'

# Do the replacement
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Only write if it actually changed
if new_content != content:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ Updated README with new quote:")
    print(new_quote)
else:
    print("⚠️ Quote unchanged. No update made.")