#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints information about a python list
 * @list: python object of class list
 * Return: nothing
*/
void print_python_list_info(PyObject *list)
{
	PyListObject *l = (PyListObject *)list;
	int i;

	printf("[*] Size of the Python List = %ld\n\n", l->ob_base.ob_size);
	printf("[*] Allocated = %ld\n\n", l->allocated);
	for (i = 0; i < l->ob_base.ob_size; i++)
		printf("Element %d: %s\n", i, l->ob_item[i]->ob_type->tp_name);
}
