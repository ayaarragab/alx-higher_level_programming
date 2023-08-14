#include "lists.h"
int main()
{
    listint_t *current;
    int n_nodes = calculate_n_nodes(head);
    current = *head;
    if (n_nodes == 0)
        return (1);
    while (current != NULL)
    {
        if (compare_nodes(current, n_nodes))
        {
            current = current->next;
            n_nodes -= 2;
        }
        else
            return (0);
    }
    return (1);
}
