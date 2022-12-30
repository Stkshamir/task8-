import re
import enchant

# Initialize the spelling checker
d = enchant.Dict("en_US")

# Define the function to correct spelling
def correct_spelling(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Correct the spelling of each word
    corrected_words = [d.suggest(word)[0] if not d.check(word) else word for word in words]
    
    # Join the corrected words into a single string
    corrected_text = " ".join(corrected_words)
    
    return corrected_text

# Test the function with some examples
examples = [
    "I hav a cat",
    "The cat sat on the mat",
    "I luv ice cream",
    "I hav a luvly cat"
]

for example in examples:
    corrected = correct_spelling(example)
    print(f"Original: {example}\nCorrected: {corrected}\n")