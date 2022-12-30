


# import libraries
import spacy
from spacy.matcher import Matcher

# load the NLP model
nlp = spacy.load("en_core_web_sm")

# create the Matcher object
matcher = Matcher(nlp.vocab)

# define the skills to look for
skills = ["Python", "Java", "C++", "SQL", "data analysis", "machine learning"]

# create a pattern for each skill
patterns = [nlp(skill) for skill in skills]

# add the patterns to the Matcher object
matcher.add("Skills", None, *patterns)

def filter_resume(resume, skills):
    # preprocess the resume text
    doc = nlp(resume)

    # match the skills in the resume
    matches = matcher(doc)

    # check if any skills were found
    if len(matches) > 0:
        return True
    else:
        return False


