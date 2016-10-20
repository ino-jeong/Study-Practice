#include <stdio.h>

int i=0,j=0,k=0;
int background = 0;
int image = 1;
int already = 2;
int blobCount[20]={0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0};

int main(){
    
    int grid[8][8] = {
        {1,1,0,0,1,1,1,1},
        {0,0,1,0,0,1,0,1},
        {0,0,0,0,0,0,1,0},
        {1,1,1,1,0,1,0,0},
        {1,0,0,0,0,0,1,0},
        {0,0,1,0,0,0,0,1},
        {0,1,1,1,0,1,0,1},
        {1,0,0,1,0,1,1,0}
    };
    
    int countCell(int x, int y){
        int result;
        if(x<0 || y<0 || x>=8 || y>=8){
            return 0;
        }
        else if (grid[y][x] != image){
            return 0;
        }
        else{
            grid[y][x] = already;
            return (1+
                countCell(x-1,y)+
                countCell(x-1,y-1)+
                countCell(x,y-1)+
                countCell(x+1,y-1)+
                countCell(x+1,y)+
                countCell(x+1,y+1)+
                countCell(x,y+1)+
                countCell(x-1,y+1)
            );
        }
    }
    
    //print grid image
    for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%d ",grid[i][j]);    
        }
        printf("\n");
    }    
    
    for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            blobCount[k]=countCell(j,i);
            if(blobCount[k] != 0){
                k++;
            }
        }
    }
    
    printf("\n\n------------------------------------------------\n\n");
    
    //print grid image
    for(i=0;i<8;i++){
        for(j=0;j<8;j++){
            printf("%d ",grid[i][j]);    
        }
        printf("\n");
    }
    
    printf("\n\n------------------------------------------------\n\n");
    
    //print count result
    for(i=0;i<10;i++){
        if(blobCount[i] != 0){
            printf("size of blob no.%d = %d\n",(i+1),blobCount[i]);
        }
    }

    return 0;
}
