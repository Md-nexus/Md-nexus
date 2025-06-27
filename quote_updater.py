import random

quotes = [
    "Simplicity is the soul of efficiency.",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Every bug is a lesson in disguise.",
    "Build what you need. Break what you don't.",
    "In the middle of difficulty lies opportunity. – Einstein"
]

# Load README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace between the quote markers
start = "<!--QUOTE_START-->"
end = "<!--QUOTE_END-->"

before = content.split(start)[0]
after = content.split(end)[1]

quote = f'{start}\n🧠 **Daily Thought:** *"{random.choice(quotes)}"*\n{end}'
new_content = f"{before}{quote}{after}"

# Write back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)