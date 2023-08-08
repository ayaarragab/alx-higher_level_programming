#include "lists.h"
/**
 * check_cycle - checks if a list is cyclic
 * @list: list
 * Return: 1 if cyclic zero if not
*/
int check_cycle(listint_t *list)
{
	const listint_t *head, *current = list;

	head = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == head)
			return (1);
	}
	return (0);
}
