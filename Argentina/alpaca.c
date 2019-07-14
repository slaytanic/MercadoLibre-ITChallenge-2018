/* Doubly Linked List implementation */
#include <stdio.h>
#include <stdlib.h>

struct node {
	char data;
	struct node* next;
	struct node* prev;
};

//Creates a new Node and returns pointer to it. 
struct node* new(char x, struct node* prev, struct node* next) {
	struct node* new_node = (struct node*)malloc(sizeof(struct node));
	new_node->data = x;
	new_node->prev = prev;
	new_node->next = next;
	return new_node;
}

struct node* replace(struct node* self) {
  struct node* old_next = self->next;
  struct node* old_prev = self->prev;

  if (self->data == 'A') {
    self->next = new('L', self, old_next);
    if (old_next != NULL) {
      old_next->prev = self->next;
    }
    return old_next;
  } else if (self->data == 'L') {
    struct node* p1 = new('P', old_prev, NULL);
    old_prev->next = p1;
    struct node* a1 = new('A', p1, NULL);
    p1->next = a1;
    struct node* c1 = new('C', a1, NULL);
    a1->next = c1;
    struct node* a2 = new('A', c1, old_next);
    c1->next = a2;
    if (old_next != NULL) {
      old_next->prev = a2;
    }
    free(self);
    return old_next;
  } else if (self->data == 'P') {
    self->prev = new('C', old_prev, self);
    old_prev->next = self->prev;
    return self->next;
  } else if (self->data == 'C') {
    self->prev = new('P', old_prev, self);
    old_prev->next = self->prev;
    return self->next;
  }
  return NULL;
}


int main() {
  int n = 20;
  int m = 123456789;
  struct node* head = new('A', NULL, NULL);

  for (int i = 0; i < n; i++) {
    printf("Times %i\n", i);
    struct node* curr = head;
    while (curr != NULL) {
      curr = replace(curr);
    }
  }

  struct node* curr = head;
  while (curr != NULL) {
    struct node* prev = curr; 
    printf("%c", curr->data);
    curr = curr->next;
    free(prev);
  }
  printf("\n");
}
