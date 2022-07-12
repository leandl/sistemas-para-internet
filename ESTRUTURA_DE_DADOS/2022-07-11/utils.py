import timeit

def debug(func):
  def wrapper_debug(*args, **kwargs):
    args_repr = [repr(a) for a in args]                      
    kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
    signature = ", ".join(args_repr + kwargs_repr)           
    print(f"Calling {func.__name__}({signature})")
    value = func(*args, **kwargs)
    print(f"{func.__name__!r} returned {value!r}")          
    return value
  return wrapper_debug

def timer(func):
  def wrapper_timer(*args, **kwargs):
    start_time = timeit.default_timer()
    _return = func(*args, **kwargs)
    end_time = timeit.default_timer()
    print('Duration: {}'.format(end_time - start_time))
    print('==========================================')
    return _return
  return wrapper_timer