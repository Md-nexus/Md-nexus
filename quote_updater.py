import random

# Quotes — Add more here
quotes = [
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it.",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Curiosity is the compass. Bugs are just detours."
]

# Pick a random quote
quote = random.choice(quotes)

# Load README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the section
start = "<!--QUOTE_START-->"
end = "<!--QUOTE_END-->"
before = content.split(start)[0]
after = content.split(end)[1]

new_content = f"{before}{start}\n🧠 **Daily Thought:** *\"{quote}\"*\n{end}{after}"

# Save it back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
