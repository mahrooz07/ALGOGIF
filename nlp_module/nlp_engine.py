# # # python -m spacy download en_core_web_sm ----> to download english language model

# # import spacy

# # nlp = spacy.load("en_core_web_sm")

# # text = ("When i was a little child, i loved my life so much that i bearly had time to sleep considering loosers will"
# #         " sleep all the time and especially i loved every moment but now, ahhhh! (sighs)")

# # doc = nlp(text)

# # # Analyze syntax
# # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# # # Find named entities, phrases and concepts
# # for entity in doc.ents:
# #     print(entity.text, entity.label_)  


# # Code Implementation for my model
# import spacy

# nlp = spacy.load("en_core_web_sm")

# def parse_query(query):
#         """
#         This function takes the user query and extracts the data structure and operation
#         """

#         doc = nlp(query)

#         operations = ['insert','delete','traverse','add']
#         data_structures = ['linked list','binary tree','queue','stack']

#         detected_operation = None
#         detected_structure = None

#         #Extracting structure and operation from the query

#         for token in doc:
#                 if token.lemma_ in operations:
#                         detected_operation = token.lemma_

#         for i in range(len(doc)):
#                 for structure in data_structures:
#                         structure_tokens = structure.split() # e.g. - ["linked",  "List"] - Linked list is splitted as per this 
#                         if doc[i:i + len(structure_tokens)].text.lower() == structure:
#                                 detected_structure = structure
#                                 break

#         return detected_operation, detected_structure  
# # import nltk
# # nltk.download('wordnet')
# from nltk.corpus import wordnet

# def get_synonym(word):
#     synonyms = set()
#     for syn in wordnet.synsets(word):
#         for lemma in syn.lemmas():
#             synonyms.add(lemma.name())
#     return synonyms

# # word = "eat"
# # set = get_synonym(word)
# # for i in set:
# #     print(i)  

from nltk.corpus import wordnet

def get_synonyms(word):
    """Retrieve synonyms for a word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def parse_query(query):
    """Parses the user query to identify the operation and data structure."""
    # Define base terms and synonyms for operations
    operations = {
        "insert": get_synonyms("insert"),
        "delete": get_synonyms("delete"),
        "push": {"push", "press", "shove", "thrust", "force", "propel", "drive", "insert", "advance", "send", "exert force"},
        "pop": {"pop", "remove", "extract", "take out", "pull out", "eject", "unload", "dislodge", "withdraw", "release"},
        "enqueue": {"enqueue", "add", "insert","queue up", "Add to queue", "Place in queue"},
        "dequeue": {"dequeue", "remove", "delete", "take away", "Dispose", "Discard", "Clear", "Eliminate"}
    }
    
    # Basic data structure list
    data_structures = ["linked list", "stack", "queue", "binary tree"]

    # Convert query to lowercase for case-insensitive matching
    query = query.lower()

    # Identify operation
    identified_operation = None
    for operation, synonyms in operations.items():
        if any(syn in query for syn in synonyms):
            identified_operation = operation
            break

    # Identify data structure
    identified_structure = None
    for structure in data_structures:
        if structure in query:
            identified_structure = structure
            break

    # Check if both operation and structure were identified
    if not identified_operation or not identified_structure:
        return "I couldn't understand. Try asking about insertion, deletion, or traversal with a data structure.", 400

    return identified_operation, identified_structure


        