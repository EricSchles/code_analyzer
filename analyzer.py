class PythonAnalyzer:
    """
    self.ratio := the number of lines of comments versus the number of lines of code.
    self.ave_conseq_comments := the average number of comments in a row.
    self.num_funcs := the number of functions per file
    self.num_func_calls := number of times a given function is called throughout a piece of code or a project.
    self.num_classes := the number of classes in a piece of code or project
    self.num_class_instances := the number of times the class is instantiated throughout the code base.
    self.num_linear_algo := number of O(n) code blocks
    self.num_squared_algo := number of O(n^2) code blocks
    self.num_cubed_algo := number of O(n^3) code blocks
    self.num_4th_algo := number of O(n^4) code blocks
    self.mean_ratio := the mean ratio across all the files in the code base
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
            #for each - key is file name, value is value of the data
            self.ratio = {}
            self.ave_conseq_comments = {}
            self.num_funcs = {}
            self.num_func_calls = {}
            self.num_classes = {}
            self.num_class_instances = {}
            self.num_linear_algo = {}
            self.num_squared_algo = {}
            self.num_cubed_algo = {}
            self.num_4th_algo = {}
            self.mean_ratio = {}
        else:
            if os.path.isfile(code):
                self.code = open(code,"r")
            else:
                print "didn't pass in a file, but file was expected"
                sys.exit(0)
            self.ratio = 0
            self.ave_conseq_comments = 0
            self.num_funcs = 0
            self.num_func_calls = {} #keys are the functions, values are the calls
            self.num_classes = 0
            self.num_class_instances = {} #keys are the classes, values are the counts
            self.num_linear_algo = {}
            self.num_squared_algo = {}
            self.num_cubed_algo = {}
            self.num_4th_algo = {}
            self.mean_ratio = None
        self.is_project = is_project

    def _ratio(self):
        if self.is_project:
            for pyfile in self.code:
                comments = 0
                non_comments = 0
                for line in pyfile:
                    if "#" in line:
                        comments += 1
                    else:
                        non_comments += 1
                self.ratio[pyfile] = {"comments":comments,"non_comments":non_comments,"ratio":comments/float(len(pyfile))}
        else:
            comments = 0
            non_comments = 0
            for line in self.code:
                if "#" in line:
                    comments += 1
                else:
                    non_comments += 1
            self.ratio = {"comments":comments,"non_comments":non_comments,"ratio":comments/float(len(self.code))}
                

    def _mean(self):
        if self.is_project:
            summa = sum([self.ratio[key]["ratio"] for key in self.ratio.keys()])
            self.mean_ratio = float(summa)/len(self.ratio.keys())
        else:
            self.mean_ratio = None
    def _conseq_comment_count(self):
        if self.is_project:
            
