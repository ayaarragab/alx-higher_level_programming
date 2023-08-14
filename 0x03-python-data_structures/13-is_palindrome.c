#include "lists.h"

/**
 * calculate_n_nodes - Calculate the number of nodes in the linked list.
 * @temp: Pointer to a pointer to the head of the linked list.
 * Return: Number of nodes in the linked list.
 */
int calculate_n_nodes(listint_t **temp)
{
	listint_t *current;
	unsigned int n;

	if (temp == NULL || *temp == NULL)
		return (0);

	current = *temp;
	n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * compare_nodes - Compare values of two nodes.
 * @current: Pointer to the current node.
 * @current_n: Number of the current node.
 * Return: 1 if the nodes have the same value, 0 otherwise.
 */
int compare_nodes(listint_t *current, int current_n)
{
	int i = 0;
	listint_t *trace = current;

	if (current_n == 1)
		return (1);
	else if (current_n == 2)
	{
		if (current->n == current->next->n)
			return (1);
		else
			return (0);
	}
	while (i < current_n - 1)
	{
		trace = trace->next;
		i++;
	}
	if (current->n == trace->n)
		return (1);
	else
		return (0);
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int n = calculate_n_nodes(head);
	listint_t *current;

	current = *head;

	if (n == 0)
		return (1);

	while (current != NULL)
	{
		if (compare_nodes(current, n))
		{
			current = current->next;
			n -= 2;
		}
		else
			return (0);
	}

	return (1);
}
