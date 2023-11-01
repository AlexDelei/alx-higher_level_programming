#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks is a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return:0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next; /*Move one step at a time*/
		fast = fast->next->next;/*two steps at a time*/
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
