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
 * insert_node - inserts in a sorted node
 * @head: pointer to head pointer
 * @number: number to be inserted
 * Return: new node or null
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *temp2 = *head;
	listint_t *new_node = malloc(sizeof(listint_t));
	int count = 0, i = 0;

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (number > 0)
	{
		while (temp->n < number && temp->next != NULL)
		{
			temp = temp->next;
			count++;
		}
		if (calculate_n_nodes(head) == count + 1)
		{
			temp->next = new_node;
			new_node->next = NULL;
			return (new_node);
		}
		while (i < count - 1)
		{
			temp2 = temp2->next;
			i++;
		}
	}
	else
	{
		*head = new_node;
		new_node->next = temp;
		return (new_node);
	}
	temp2->next = new_node;
	new_node->next = temp;
	return (new_node);
}
