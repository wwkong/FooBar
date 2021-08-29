#include <vector>

extern "C" {
    class Foo {
      public:
        char* desc;
        Foo(char* istr): desc(istr) {}
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
}
