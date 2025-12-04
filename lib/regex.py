#!/usr/bin/env python3
import re

# Regular expression pattern that matches sentences with specific characteristics
# This pattern matches sentences that:
# - Start with a capital letter or "It's"
# - Contain words (letters, apostrophes, spaces)
# - End with punctuation (., !, or ?)

# Pattern breakdown:
# (?:It's|[A-Z])  - Non-capturing group: matches either "It's" or a single capital letter
# [\w\s',]*       - Matches any combination of word characters, whitespace, apostrophes, or commas
# today['s]?      - Matches "today" or "today's"
# [\w\s',]*       - Matches any more characters after "today"
# [.!?]           - Matches sentence-ending punctuation

pattern = r"(?:It's|[A-Z])[\w\s',]*today['s]?[\w\s',]*[.!?]"

# Compile the regex pattern
my_regex = re.compile(pattern)