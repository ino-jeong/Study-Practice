//remove i'th node
//return data of removed node

Node *remove(int index){
    if(index < 0){
        return NULL;
    }
    if(index == 0){
        return remove_first();
    }
    
    Node *prev = get_node(index-1);
    if(prev==NULL){
        return NULL;
    }
    else{
        return remove_after(prev); //remove_after() will return removed node's address
    }
}



//remove by item

Node *remove(char *item){
    Node *p = head;
    Node *q = NULL;
    
    while(p!=NULL && strcmp(p->data, item)!=0){
        q=p;
        p=p->next;
    }
    
    if(p==NULL){ //end of linked list
        return NULL;
    }
    if(q==NULL){ //at the begining
        return remove_first();
    }
    else{
        return remove_after(q);
    }
}



