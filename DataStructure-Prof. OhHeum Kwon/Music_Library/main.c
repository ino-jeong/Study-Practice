#include <stdio.h>
#include "string_tools.h"
#include <stdlib.h>
#include <string.h>
#define BUFFER_LENGTH 200

void process_command();
void handle_add();

int main()
{
    process_command();
    
    return 0;
}

void process_command(){
    
    char command_line[BUFFER_LENGTH];
    char *command;
    while(1){
        printf("$ "); //prompt
        
        if(read_line(stdin,command_line, BUFFER_LENGTH) <= 0){
            continue;
        }
        
        command = strtok(command_line," ");
        if(strcmp(command,"add")==0)
            handle_add();
            
            /*
            
        else if(strcmp(command,"search")==0)
            handle_search();
        else if(strcmp(command,"remove")==0)
            handle_remove();
        else if(strcmp(command,"status")==0)
            handle_status();
        else if(strcmp(command,"play")==0)
            handle_play();
        else if(strcmp(command,"save")==0)
            handle_save();
            
            */
            
        else if(strcmp(command,"exit")==0)
            break;
        
    }
}



void handle_add(){
    
    char buffer[BUFFER_LENGTH];
    char *artist=NULL, *title=NULL, *path=NULL;
    
    printf("\tArtist : ");
    
    if(read_line(stdin, buffer, BUFFER_LENGTH)>0)
        artist = strdup(buffer);
    
    printf("\tTitle : ");
        
    if(read_line(stdin, buffer, BUFFER_LENGTH)>0)
        title = strdup(buffer);
    
    printf("\tPath : ");
    
    if(read_line(stdin, buffer, BUFFER_LENGTH)>0)
        path = strdup(buffer);
        
    printf("%s %s %s\n",artist,title,path);
        
    /*add to the music library*/
    
    add_song(artist,title,path);
    
}













//
