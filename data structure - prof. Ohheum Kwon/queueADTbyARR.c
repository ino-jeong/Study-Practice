#include <stdio.h>
#include <stdlib.h>
#include "queueADTbyARR.h"

#define INIT_CAPACITY 100

struct queue_type {
    Item *contents; //array by malloc
    int front;
    int rear;
    int size; //number of stored data
    int capacity; //size of array
};

void terminate(const char *message){
    printf("%s\n", message);
    exit(1);
}

int get_size(Queue q){
    return q->size;
}

Queue create(){
    Queue q = (Queue)malloc(sizeof(struct queue_size));
    if(q==NULL)
        terminate("malloc error\n");
    
    q->contents = (Item *)malloc(INIT_CAPACITY * sizeof(Item));
    
    if(q->contents == NULL){
        free(q);
        terminate("array malloc error.\n");
    }
    
    q->front = 0;
    q->rear = -1;
    q->size = 0;
    q->capacity = INIT_CAPACITY;
    
    return q;
}

void destroy(Queue q){
    free(q->contents);
    free(q);
}


void make_empty(Queue q){
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}

bool is_empty(Queue q)
{
    return (q->size == 0);
}

bool is_full(Queue q){
    return (q->size == q->capacity);
}


void enqueue(Queue q, Item i){
    if(is_full(q))
        reallocate(q);
        
    q->rear = (q->rear + 1)%(q->capacity);
    q->contents[q->rear] = i;
    q->size++;
}

Item dequeue(Queue q){
    if(is_empty(q))
        terminate("error.");
    
    Item result = q->contents[q->front];
    q->front = (q->front+1) % (q->capacity);
    q->size--;
    
    return result;
}


Item peek(Queue q){
    if(is_empty(q))
        terminate("error : queue is empty\n");
        
    return (q->contents[q->front]);
}


void reallocate(Queue q){
    Item *tmp = (Item *)malloc(2* (q->capacity) * sizeof(Item));
    if(tmp == NULL)
        terminate("reallocate malloc error.");
    
    int j = q->front;
    int i=0;
    for(i=0; i<(q->size); i++){
        tmp[i]=q->contents[j];
        j=(j+1)%(q->capacity);
    }
    
    free(q->contents);
    
    q->front = 0;
    q->rear = q->size-1;
    q->contents = tmp;
    q->capacity *=2;
}





