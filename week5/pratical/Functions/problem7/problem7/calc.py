from pretty_print import simple_print


from pretty_print import pro_print


def calculate_cube(x):
    return x*x*x

def calculate_square(x):
    return x*x 

def main():
    y = calculate_square(2)
    simple_print(y)
    f = calculate_cube(4)
    pro_print(f)

main()