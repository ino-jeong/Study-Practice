#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    char *data;
    struct node *next;
} Node;

Node *top = NULL;

void push(char *item);
char* pop();
char* peek();
int is_empty();


void push(char* item){
    Node *p = (Node *)malloc(sizeof(Node));
    p->data = item;
    p->next = top;
    top = p;
}

char *pop(){
    Node *p = top;
    
    if(is_empty()){
        return NULL;
    }
    char *result = top->data;
    top = top->next;
    free(p);
    return result;
}

char *peek(){
    if(is_empty()){
        return NULL;
    }
    return top->data;
}

int is_empty(){
    return (top==NULL);
}
