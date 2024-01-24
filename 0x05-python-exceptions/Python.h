#ifndef PYTHON_H
#define PYTHON_H

#include <stdio.h>

typedef struct {
    int dummy;
} PyObject;

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif /* PYTHON_H */
