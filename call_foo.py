from ctypes import c_char_p, c_void_p
import ctypes, os
libfoo = ctypes.CDLL(os.getcwd() + '/foo.so')
libfoo.Foo_get.restype = c_char_p

# # GOOD CODE
# libfoo.Foo_new.argtype = [c_char_p]
# libfoo.Foo_set.argtype = [c_void_p, c_char_p]

class Foo:
    def __init__(self, istr):

        # # GOOD CODE
        # istr = bytes(istr, 'utf-8')
        # self.foo = libfoo.Foo_new(c_char_p(istr))

        # BAD CODE
        self.foo = libfoo.Foo_new(istr)

    def set_desc(self, new_str):

        # # GOOD CODE
        # new_str = bytes(new_str, 'utf-8')
        # libfoo.Foo_set(self.foo, c_char_p(new_str))

        # BAD CODE
        libfoo.Foo_set(self.foo, new_str)

    def get_desc(self):
        return ("Printing the contents of Foo from Python: " + str(libfoo.Foo_get(self.foo)))

    def print_desc(self):
        libfoo.Foo_print(self.foo)

    def print_ref(self):
        libfoo.Foo_ref(self.foo)

x = Foo("Here is a random string")
x.print_ref()
x.set_desc("Here is a new string")
print(x.get_desc())
x.print_desc()
y = Foo("blah")  # Add/remove this line to toggle this new problem
y.print_ref()
print(x.get_desc())
x.print_desc()
