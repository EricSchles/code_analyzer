class PythonAnalyzer:
    def __init__(self,code,is_project=False):
        if is_project:
            if os.path.isdir(code):
                glob(code+"/*.py")
        else:
            if os.path.isfile(code):
                self.code = open(code,"r")
            else:
                print "didn't pass in a file, but file was expected"
        
