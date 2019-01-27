class TtlGenerator:
    """
        Class for writing Turtle file with fact's factid &
        confidence with the given format
    """

    def __init__(self, filename):
        self.filename = filename

        fileName = Path("output/"+filename + ".ttl")

        if fileName.is_file():
            self.f = open("output/" + filename + '.ttl', "w")
        else:
            try:
                os.makedirs(os.path.dirname(fileName))
                self.f = open("output/" + filename + '.ttl', "w")
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def addfact(self, factid, confidence):
        self.f.write('<http://swc2017.aksw.org/task2/dataset/' + factid + '> '
                     + '<http://swc2017.aksw.org/hasTruthValue> '
                     + '"' + confidence + '"' + '^^<http://www.w3.org/2001/XMLSchema#double> .\n')

    def closefile(self):
        self.f.close()
