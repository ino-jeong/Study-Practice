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



//Linked list traversal (as data value)
//return matched node's pointer

Node *find(char *word){
    Node *p = head;
    
    while(p!=NULL){
        if(strcmp(p->data, word)==0){
            return p;
        }
        p = p->next;
    }
    return NULL;
}



//return i'th node's pointer (counting from 0)
Node *get_node(int index){
    if (index < 0){
        return NULL;
    }
    
    Node *p = head;
    for(int i=0; (i<index && p!=NULL); i++){
        p=p->next;
    }
    return p;
}



//add by index
//add new node as i'th node
//return 0 if failed, and 1 if success
//assume head is global variable

int add(int index, char *item){
    if(index < 0){
        return 0;
    }
    
    if(index == 0){
        add_first(item);
        return 1;
    }
    
    Node *prev = get_node(index-1); //obtain previous node of target
    if(prev != NULL){
        add_after(prev, item);
        return 1;
    }
    
    return 0; //adding process is failed if process reach this statement.
} 
