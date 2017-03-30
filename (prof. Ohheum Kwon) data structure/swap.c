/**********************************************************
swap vs. swap by pointer practice.
**********************************************************/

#include <stdio.h>

void swap1(int x, int y){
    int temp = x;
    x=y;
    y=temp;
    
    printf("x %d y %d (swap1)\n",x,y);
    
}

void swap2(int* x, int* y){
    int* temp;
    *temp = *x;
    *x=*y;
    *y=*temp;
    
    printf("x %d y %d (swap2)\n",*x,*y);
    
}

int main()
{
    int x = 7;
    int y = 9;
    int* xx = &x;
    int* yy = &y;
    
    printf("x %d y %d\n",x,y);
    swap1(x,y);
    printf("x %d y %d\n",x,y);

    printf("\n===============================\n\n");

    printf("x %d y %d\n",*xx,*yy);
    swap2(xx,yy);
    printf("x %d y %d\n",*xx,*yy);

    return 0;
}

