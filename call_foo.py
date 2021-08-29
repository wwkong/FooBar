import ctypes, os
libfoo = ctypes.CDLL(os.getcwd() + '/foo.so')
libfoo.Foo_get.restype = ctypes.c_char_p
libfoo.Foo_new.argtype = ctypes.c_char_p
libfoo.Foo_set.argtype = ctypes.c_void_p, ctypes.c_char_p

class Foo:
    def __init__(self, istr):
        # self.foo = libfoo.Foo_new(istr.encode('utf-8'))
        self.foo = libfoo.Foo_new(istr)

    def set_desc(self, new_str):
        # libfoo.Foo_set(self.foo, new_str.encode('utf-8'))
        libfoo.Foo_set(self.foo, new_str)

    def get_desc(self):
        return libfoo.Foo_get(self.foo)

x = Foo("Here is a random string")
x.set_desc("Here is a new string")
print(x.get_desc())

