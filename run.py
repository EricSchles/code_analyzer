from analyzer import PythonAnalyzer as anlz

p = anlz("bst_pure.py")
print p.ratio, p.ave_conseq_comments, 
print p.num_funcs, p.num_func_calls
print p.num_classes, p.num_class_instances
