def multiply(x):
    def inner(y):
        def func(z):
            return x*y*z
        return func
    return inner


multyply_ten = multiply(10)
