//insert after specific node.
//using Node pointer prev to indicate specific node.
//return 1 when its work is done successfully, and return 0 when it is failed.

int add_after(Node *prev, char *item){
    if(prev == NULL){
        return 0;
    }
    
    Node *temp = (Node *)malloc(sizeof(Node));
    temp->data = item;
    temp->next = prev->next;
    prev->next = temp;
    
    return 1;
}



//remove first(head) node.
//return removed node's address.
//returned node shall be freed.

Node *remove_first(){
  //if head is NULL, return NULL
  if(head==NULL){
    return NULL;
  }
  else{
    Node *temp = head;
    head = head->next;
    return temp; //temp shall be freed after this function is terminated.
  }
}



//remove after
//return removed node's pointer

Node *remove_after(Node *prev){
    Node *temp = prev->next;
    
    if(temp == NULL){
        return NULL;
    }
    else{
        prev->next = temp->next; // prev->next = prev->next->next
        return temp;
    }
}



