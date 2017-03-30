//general add function. when head is global variable
//adding new node as first node.

void add_first(char *item){
  Node *temp = (Node *)malloc(sizeof(Node));
  temp->data = item;
  temp->next = head;
  head = temp;
}


//when head is local variable(1). call as bellow :
//add_first(&head, item_to_store)

void add_first(Node **ptr_head, char *item){
  Node *temp = (Node *)malloc(sizeof(Node));
  temp->data = item;
  temp->next = *ptr_head;
  *ptr_head = temp;
}


//when head is local variable(2). call as bellow :
//head=add_first(head, item_to_store)

Node *add_first(Node *head, char *item){
  Node *temp = (Node *)malloc(sizeof(Node));
  temp->data = item;
  temp->next = head;
  return temp;
}
