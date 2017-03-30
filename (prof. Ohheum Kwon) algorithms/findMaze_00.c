#include <stdio.h>
typedef int bool;
#define true 1
#define false 0

int main()
{
    int maze[8][8]={
        {0,0,0,0,0,0,0,1},
        {0,1,1,0,1,1,0,1},
        {0,0,0,1,0,0,0,1},
        {0,1,0,0,1,1,0,0},
        {0,1,1,1,0,0,1,1},
        {0,1,0,0,0,1,0,1},
        {0,0,0,1,0,0,0,1},
        {0,1,1,1,0,1,0,0}
    };
    
    int i=0,j=0;
    
    int pathway=0;
    int wall=1;
    int blocked=2;
    int path=3;
    
    bool findMaze(int x, int y){
        if(x<0 || y<0 || x>=8 || y>=8){
            return false;
        }
        else if (maze[y][x] != pathway){
            return false;
        }
        else if (x==7 && y==7){
            maze[y][x] = path;
            return true;
        }
        else{
            maze[y][x] = path;
            if(findMaze(x-1,y) || findMaze(x,y+1) || findMaze(x+1,y) || findMaze(x,y-1)){
                return true;    
            }
            maze[y][x] = blocked;
            return false;
        }
    
    }
    
    for (i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%d",maze[i][j]);    
        }
        printf("\n");
    }
    
    findMaze(0,0);
    
    printf("\n--------------------------------\n");
    
    for (i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%d",maze[i][j]);    
        }
        printf("\n");
    }


    return 0;
}

