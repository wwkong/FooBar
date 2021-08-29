#include <vector>
#include <iostream>
#include <stdio.h>

extern "C" {
    class Foo {
      public:
        char* desc;
        Foo(char* istr): desc(istr) {
            printf("Initializing Foo with string: %s\n", istr);
        }
    };
    Foo* Foo_new(char* bar) {
        return new Foo(bar);
    }
    void Foo_set(Foo *foo, char* new_bar) {
        foo->desc = new_bar;
    }
    char* Foo_get(Foo *foo) {
        return foo->desc;
    }
    void Foo_print(Foo *foo) {
        printf("Printing the contents of Foo from C++: %s\n", foo->desc);
    }
    void Foo_ref(Foo *foo) {
        std::cout << "The address of this object is: " << foo << std::endl;
    }

}
