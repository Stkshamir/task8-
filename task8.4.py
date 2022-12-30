# import libraries
import spacy
from spacy.matcher import Matcher

# load the NLP model
nlp = spacy.load("en_core_web_sm")

# create the Matcher object
matcher = Matcher(nlp.vocab)

# define the patterns for the Matcher object
pattern1 = [{"LOWER": "hi"}, {"LOWER": "i"}, {"LOWER": "want"}, {"LOWER": "to"}, {"LOWER": "book"}, {"LOWER": "a"}, {"LOWER": "room"}]
pattern2 = [{"LOWER": "what"}, {"LOWER": "are"}, {"LOWER": "the"}, {"LOWER": "room"}, {"LOWER": "rates"}]
pattern3 = [{"LOWER": "i"}, {"LOWER": "would"}, {"LOWER": "like"}, {"LOWER": "to"}, {"LOWER": "book"}, {"LOWER": "a"}, {"LOWER": "room"}, {"LOWER": "from"}, {"LOWER": "*arrival date*"}, {"LOWER": "to"}, {"LOWER": "*departure date*"}]
pattern4 = [{"LOWER": "do"}, {"LOWER": "you"}, {"LOWER": "have"}, {"LOWER": "availability"}, {"LOWER": "for"}, {"LOWER": "*room type*"}, {"LOWER": "rooms"}]
pattern5 = [{"LOWER": "how"}, {"LOWER": "much"}, {"LOWER": "will"}, {"LOWER": "it"}, {"LOWER": "cost"}]
pattern6 = [{"LOWER": "i"}, {"LOWER": "accept"}, {"LOWER": "the"}, {"LOWER": "cancellation"}, {"LOWER": "policy"}]
pattern7 = [{"LOWER": "book"}, {"LOWER": "the"}, {"LOWER": "room"}]

# add the patterns to the Matcher object
matcher.add("Booking", None, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7)

# define the chatbot's response function
def chatbot_response(doc):
    # match the user's input to a pattern
    matches = matcher(doc)
    for match_id, start, end in matches:
        # get the matched span
        span = doc[start:end]
        # check which pattern was matched
        if span.text.lower() == "hi, i want to book a room":
            return "Hi! I'm here to help you book a room. May I have your name, please?"
        elif span.text.lower() == "what are the room rates":
            return "Our room rates vary depending on the type of room and the time of year. Would you like to see our current rates?"
        elif span.text.lower() == "i would like to book a room from *arrival date* to *departure date*":
            return "Sure, let me check our availability for those dates. Can you please provide your name and a government-issued ID as proof of identity?"
        elif span.text.lower() == "do you have availability for *room type* rooms":
            return