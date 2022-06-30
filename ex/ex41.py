import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, ***)":
        "class%%% has-a function *** that take self and @@@ params",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
print(f"Print out PHRASE_FIRST {PHRASE_FIRST}\n")  # To understand

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    print(f"Print out class_names {class_names}\n")  # To understand
    other_names = random.sample(WORDS, snippet.count("***"))
    print(f"Print out other_names {other_names}\n")  # To understand
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        print(f"Print out param_count {param_count}\n")  # To understand
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        print(f"Print out param_names {param_names}\n")  # To understand

    for sentence in snippet, phrase:
        print(f"Print out snippet {snippet}\n")  # To understand
        print(f"Print out phrase {phrase}\n")  # To understand
        print(f"Print out sentence {sentence}\n")  # To understand
        result = sentence[:]
        print(f"Print out result {result}\n")  # To understand

        # fake class name
        for word in class_names:
            result = result.replace("%%%", word, 1)
        print(f"Print out result 1 {result}\n")  # To understand

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        print(f"Print out result 2 {result}\n")  # To understand

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        print(f"Print out result 3 {result}\n")  # To understand

        results.append(result)

    print(f"Print out results {results}\n")  # To understand
    return results


# keep going until they hit Ctrl-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        print(f"Print out snippets{snippets}\n")  # To understand

        for snippet in snippets:
            phrase = PHRASES[snippet]
            print(f"Print out snippet {snippet}\n")  # To understand
            print(f"Print out phrase {phrase}\n")  # To understand
            question, answer = convert(snippet, phrase)
            print(f"Print out question {question}\n")  # To understand
            print(f"Print out answer {answer}\n")  # To understand
            if PHRASE_FIRST:
                question, answer = answer, question
                print(f"Print out question {question}\n")  # To understand
                print(f"Print out answer {answer}\n")  # To understand
            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

