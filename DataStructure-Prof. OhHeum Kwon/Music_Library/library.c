#include "library.h"
#include <stdio.h>

Artist *artist_directory[NUM_CHARS];
int num_index = 0;

int i=0;
void initialize(){
    for(i =0; i<NUM_CHARS; i++){
        artist_directory[i] = NULL;
    }
}

Artist *create_artist_instance(char *name){
    
    Artist *ptr_artist = (Artist *)malloc(sizeof(Artist));
    ptr_artist->name = name;
    ptr_artist->head = NULL;
    ptr_artist->tail = NULL;
    ptr_artist->next = NULL;
    
    return ptr_artist;
}


Artist *add_artist(char *name){
    Artist *ptr_artist = create_artist_instance(name);
    
    Artist *p = artist_directory[(unsigned char)name[0]];
    Artist *q = NULL;
    
    while(p!=NULL && strcmp(p->name,name)<0){
        q=p;
        p=p->next;
    }
    
    if(p==NULL && q==NULL){
        artist_directory[(unsigned char)name[0]] = ptr_artist;
    }
    else if(q==NULL){
        ptr_artist->next=artist_directory[(unsigned char)name[0]];
        artist_directory[(unsigned char)name[0]]=ptr_artist;
    }
    else{
        ptr_artist->next = p;
        q->next = ptr_artist;
    }
    
    return ptr_artist;
    
}

Song *create_song_instance(Artist *ptr_artist, char *title, char *path){
    Song *ptr_song = (Song *)malloc(sizeof(Song));
    ptr_song->artist = ptr_artist;
    ptr_song->title = title;
    ptr_song->path = path;
    ptr_song->index = num_index;
    num_index++;
    
    return ptr_song;
}

void add_song(char *artist, char *title, char *path){
    //find if the artist exists already
    Artist *ptr_artist = find_artist(artist);
    if(ptr_artist == NULL){
        ptr_artist = add_artist(artist);
    }
    
    Song *ptr_song = create_song_instance(ptr_artist,title,path);
    Snode *ptr_snode = (Snode *)malloc(sizeof(Snode));
    ptr_snode->song = ptr_song;
    ptr_snode->next = NULL;
    ptr_snode->prev = NULL;
    
    insert_node(ptr_artist, ptr_snode);
}

void insert_node(Artist *ptr_artist, Snode *ptr_snode){
    Snode *p = ptr_artist->head;
    while(p!=NULL && strcmp(p->song->title, ptr_snode->song->title)<0){
        p=p->next;
    }
    
    // add ptr_snode before p
    // case : 1.empty, 2.at the front, 3.at the end, 4.in middle
    
    if(ptr_artist->head == NULL){ // case 1
        ptr_artist->head = ptr_snode;
        ptr_artist->tail = ptr_snode;
    }
    else if(p == ptr_artist->head){ // case 2
        ptr_snode->next = ptr_artist->head;
        ptr_artist->head->prev = ptr_snode;
        ptr_artist->head = ptr_snode;
    }
    else if(p == NULL){ // case 3
         ptr_snode->prev = ptr_artist->tail;
         ptr_artist->tail->next = ptr_snode;
         ptr_artist->tail = ptr_snode;
    }
    else{ // case 4
        ptr_snode->next = p;
        ptr_snode->prev = p->next;
        p->prev->next = ptr_snode;
        p->prev = ptr_snode;
    }
}

Artist *find_artist(char *name){
    
    Artist *p = artist_directory[(unsigned char)name[0]]; //first artist with initial name[0]
    while(p!=NULL && strcmp(p->name , name) < 0){
        p=p->next;
    }
    
    if(p != NULL && strcmp(p->name, name) == 0)
        return p;
    else
        return NULL;
    
}


void status(){
    int i=0;
    for (i=0; i<NUM_CHARS; i++){
        
        Artist *p = artist_directory[i];
        while(p!=NULL){
            print_artist(p);
            p=p->next;
        }
        
    }
}


void print_artist(Artist *p){
    printf("%s\n",p->name);
    Snode *ptr_snode = p->head;
    while (ptr_snode != NULL){
        print_song(ptr_snode -> song);
        ptr_snode = ptr_snode->next;
    }
}

void print_song(Song *ptr_song){
    printf("\t%d: %s, %s\n",ptr_song->title, ptr_song->path);
}

//
