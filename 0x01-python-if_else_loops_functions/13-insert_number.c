#include "lists.h"
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

	if (*head == NULL)
	{
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}
	if (number > 0)
	{
		while (temp->n < number)
		{
			temp = temp->next;
			count++;
		}
		while (i < count - 1)
		{
			temp2 = temp2->next;
			i++;
		}
	}
	else
	{
		new_node->n = number;
		*head = new_node;
		new_node->next = temp;
		return (new_node);
	}
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	temp2->next = new_node;
	new_node->next = temp;
	return (new_node);
}
