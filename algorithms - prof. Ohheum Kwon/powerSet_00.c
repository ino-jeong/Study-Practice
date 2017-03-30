#include <stdio.h>
typedef int bool;
#define true 1
#define false 0

int n = 4;
int i = 0;
int set = 1;
char data[4]={'a','b','c','d'};
char inc[4]={false,false,false,false};

void powerSet(int k){
    
    if(k == n){
        
        printf("Set no. %d : ", set);
        set++;
        
            for(i=0 ; i<n ; i++){
                if(inc[i] == true){
                    printf("%c", data[i]);
                }
            }
            
        printf("\n");
        return;
        
    }
    
    inc[k]=false;
    powerSet(k+1);
    inc[k]=true;
    powerSet(k+1);
    
}

int main()
{
    printf("=====start print=====\n", inc[3]);
    powerSet(0);

    return 0;
}
