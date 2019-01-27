"""
Creates a corpus from Wikipedia dump file.
"""

import sys
from gensim.corpora import WikiCorpus


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


def make_corpus(in_f, out_f):

	"""Convert WikiPedia xml dump file to text corpus"""

	output = open(out_f, 'w')
	wiki = WikiCorpus(in_f)

	i = 0
	for text in wiki.get_texts():
		output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
		if i % 10000 == 0:
			print('Processed ' + str(i) + ' articles')
	output.close()
	print('Processing complete!')


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('Usage: python create_corpus.py <wikipedia_dump_file>')
		sys.exit(1)

	in_f = sys.argv[1]
	out_f = "en_wiki"

	if is_accessible(in_f):
		make_corpus(in_f, out_f)
	else:
		print("File Not Accessible")

