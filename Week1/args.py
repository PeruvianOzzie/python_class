# Rule: params, *args, default parameters, **kwargs


def arg_demo(pos1, pos2, *args, **kwargs):
    print(f"Positional params: {pos1}, {pos2}")
    print('*args:')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for key, value in kwargs.items():
        print(f"  {key}: {value}")




arg_demo('A', 'B', 1, 2, 3, 4, color='red', size='big', shape='circle')