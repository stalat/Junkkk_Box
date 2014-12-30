def foo(*args):
    current_frame = inspect.currentframe()
    previous_frame = current_frame.f_back
    traceback_obj = inspect.getframeinfo(previous_frame)

    print "Caller info :"
    print "filename: %s" % traceback_obj.filename
    print "lineno: %s" % traceback_obj.lineno
    # print "function: %s" % traceback_obj.function
    # print "code context: %s" % traceback_obj.code_context
    # print "index: %s" % traceback_obj.index
    
    if 'self' in previous_frame.f_locals:
        obj = previous_frame.f_locals['self']
        print "class %s, method %s" % (obj.__class__.__name__, previous_frame.f_code.co_name)
    else:
        print "called from %s" % previous_frame.f_code.co_name
