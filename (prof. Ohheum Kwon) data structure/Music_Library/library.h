#ifndef LIBRARY_H
#define LIBRARY_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NUM_CHARS 256
#define BUFFER_LENGTH 200

typedef struct artist Artist;
typedef struct song Song;
typedef struct snode Snode;


struct song{
    Artist *artist;
    char *title;
    char *path;
    int index;
};

struct snode{
    struct snode *next, *prev;
    Song *song;
};

struct artist {
    char *name;
    struct artist *next;
    Snode *head, *tail;
};


void add_song(char *artisst, char *title, char *path);
void initialize();
Artist *find_artist(char *name);
Artist *add_artist(char *name);
Artist *create_artist_instance(char *name);
Song *create_song_instance(Artist *ptr_artist, char *title, char *path);
void add_song(char *artist, char *title, char *path);
void insert_node(Artist *ptr_artist, Snode *ptr_snode);
void status();
void print_artist(Artist *p);
void print_song(Song *ptr_song);
void load(FILE *fp);
void search_song2(char* artist, char *title);
void search_song1(char* artist);


#endif
