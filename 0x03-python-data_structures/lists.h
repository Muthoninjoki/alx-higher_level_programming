#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
* struct listint_s - linked list
* @n:int
* @next:shows next node
* Description:node structure
*/

typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
listint_t *add_nodeint_end(listint_t **head, const int n);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
