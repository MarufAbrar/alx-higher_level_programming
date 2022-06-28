#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *mbuzi, *kondoo;

	if (list == NULL || list->next == NULL)
		return (0);

	mbuzi = list->next;
	kondoo = list->next->next;

	while (mbuzi && kondoo && kondoo->next)
	{
		if (mbuzi == kondoo)
			return (1);

		mbuzi = mbuzi->next;
		kondoo = kondoo->next->next;
	}

	return (0);
}
