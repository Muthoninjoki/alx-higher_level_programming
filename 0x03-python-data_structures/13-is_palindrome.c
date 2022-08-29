#include "lists.h"

/**
* is_palindrome - recursive palind
* @head: head list
* Return: 0 if not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);
}

/**
* aux_palind - check if it is palindrome
* @head: list
* @end: end list
*/

int aux_palind(listint_t **head, listint_t *end)
{
if (end == NULL)
return (1);

if (aux_palind(head, end->next) && (*head)->n == end->n)
{
*head = (*head)->next;
return (1);
}
return (0);
}
