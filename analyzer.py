class PythonAnalyzer:
    """
    self.ratio := the number of lines of comments versus the number of lines of code.
    self.average_num_lines := the average number of comments in a row.
    """
    def __init__(self,code,is_project=False):
        if is_project:
            if os.path.isdir(code):
                pyfiles = glob(code+"/*.py")
                self.code = []
                for pyfile in pyfiles:
                    tmp = open(pyfile,"r")
                    self.code.append(tmp)
            else:
                print "didn't pass in a file, but a file was expected"
                sys.exit(0)
            self.ratio = []
            
        else:
            if os.path.isfile(code):
                self.code = open(code,"r")
            else:
                print "didn't pass in a file, but file was expected"
                sys.exit(0)
            self.ratio = 0
        self.is_project = is_project

    def _ratio(self):
        if self.is_project:
            for 
    def mean(self):
        
