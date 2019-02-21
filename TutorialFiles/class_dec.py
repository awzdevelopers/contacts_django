def Function(fun):

    def fun2():
        print("start")
        fun()
        print("end")
    return fun2


@Function
def fun3():
    print("this is a arg function")

fun3()
