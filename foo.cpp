#include <vector>
#include <iostream>
#include <stdio.h>
#include <string.h>

extern "C" {
    class Foo {
      public:
        char* desc;
        Foo(char* istr) {
            size_t n = strlen(istr);
            desc = (char*) malloc(n * sizeof(char));
            strncpy(desc, istr, n * sizeof(char));
            printf("Initializing Foo with string: %s\n", istr);
        }
    };
    Foo* Foo_new(char* bar) {
        return new Foo(bar);
    }
    void Foo_set(Foo *foo, char* new_str) {
        size_t n = strlen(new_str);
        foo->desc = (char*) malloc(n * sizeof(char));
        strncpy(foo->desc, new_str, n * sizeof(char));
        printf("Updating Foo with new string: %s\n", new_str);
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
