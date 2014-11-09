class PythonAnalyzer:
    """
    self.ratio := the number of lines of comments versus the number of lines of code.
    self.average_num_lines := the average number of comments in a row.
    self.num_funcs := the number of functions per file
    self.num_func_calls := number of times a given function is called throughout a piece of code or a project.
    self.num_classes := the number of classes in a piece of code or project
    self.num_class_instances := the number of times the class is instantiated throughout the code base.
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
            self.average_num_lines = []
            self.num_funcs = []
            self.num_func_calls = {}
            self.num_classes = []
            self.num_class_instances = {}
        else:
            if os.path.isfile(code):
                self.code = open(code,"r")
            else:
                print "didn't pass in a file, but file was expected"
                sys.exit(0)
            self.ratio = 0
            self.average_num_lines = 0
            self.num_funcs = 0
            self.num_func_calls = {}
            self.num_classes = 0
            self.num_class_instances = {}
        self.is_project = is_project

    def _ratio(self):
        if self.is_project:
            for 
    def mean(self):
        
