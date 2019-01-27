# Builtin
import sys

# 3rd parties
import wikipedia

from ttl_generator import TtlGenerator
from extract_ner import extract_nn


def check_corpus(entities):
    return -1


def check_wikipedia(entities):
    """
        Really naive approach which first search WikiPage for the Subject
        and then try to search Object in that page and if found return
        positive confidence otherwise negative
    """
    weight = -1
    try:
        search_result = wikipedia.page(entities[0])
        content = search_result.content
    except wikipedia.exceptions.DisambiguationError:
        # Exception can be raise if search term (Subject) returns
        # multiple search result
        return 0
    except:
        return 0

    for entity in entities[1:]:
        if entity.strip():
            if content.find(entity) > -1:
                weight = 1
            else:
                return 0
    return weight


def is_accessible(p):
    """
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    mode = 'r'

    try:
        f = open(p, mode)
        f.close()
    except IOError:
        return False
    return True


if __name__ == "__main__":
    """
        Script only takes one argument which should be 
        either train or test and all extra arguments
        would be ignore
    """
    if len(sys.argv) > 1 and ['train', 'test'].index(sys.argv[1]) != -1:
        option = sys.argv[1]

        path = "data/" + option + ".tsv"

        if is_accessible(path):
            data = open("data/" + option + ".tsv", encoding="latin-1").read()
            ttl_writer = TtlGenerator("result_" + option)

            if is_accessible("en_wiki"):
                for line in data.splitlines()[1:]:
                    split = line.split("\t")

                    if len(split) < 2:
                        continue

                    factID = split[0]
                    sentence = split[1]

                    enr = extract_nn(sentence)
                    result = check_corpus(enr)

                    ttl_writer.addfact(factID, str(result))
            else:
                for line in data.splitlines()[1:]:
                    split = line.split("\t")

                    if len(split) < 2:
                        continue

                    factID = split[0]
                    sentence = split[1]

                    enr = extract_nn(sentence)
                    result = check_wikipedia(enr)

                    ttl_writer.addfact(factID, str(result))

            ttl_writer.closefile()
        else:
            print("File Not Accessible")

    else:
        print("No or Invalid arguments provided! \ntry: \n\tpython3 fact_checker.py train \nor\n\tpython3 fact_checker.py test")
