#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int isPalindrome;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	listint_t *mid = NULL;

	isPalindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);
	isPalindrome = compare_lists(*head, second_half);
	second_half = reverse_list(second_half);

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
	return (isPalindrome);
}
