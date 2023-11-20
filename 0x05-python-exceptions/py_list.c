#include "main.h"
/**
 *print_python_list - info of a list
 *@p:pointer to object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	const char *typeName;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		typeName = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, typeName);
	}
}
