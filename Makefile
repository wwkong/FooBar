all: foo.cpp
	g++ -shared -Wl,-soname,foo -o foo.so -fPIC foo.cpp
