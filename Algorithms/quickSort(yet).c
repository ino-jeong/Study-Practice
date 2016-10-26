/****************************************************************
quicksort practice (not completed yet).
****************************************************************/
#include <stdio.h>

int A[8]={5,7,8,1,-10,99,1092,0}; 

void swap(int* x, int* y){
    
    int* temp;
    *temp = *x;
    *x = *y;
    *y = *temp;
    
}

int partition(int* A, int p, int r){
    int x = 0;
    x = *(A+r);
    int i = p-1;
    int j = 0;
    
    for (j=p ; j < (r-1) ; j++){
        if(*(A+j) <= x){
            i++;
            swap((A+i),(A+j));
        }
    }
    
    swap((A+i+1),(A+r));
    
    return (i+1);
    
}

void quickSort(int* A, int p, int r){
    int q=0;
    
    if(p<r){
        q=partition(A,p,r);
        quickSort(A,p,(q-1));
        quickSort(A,(q+1),r);
    }
    
}

int main()
{
    int k=0;
    
    for(k=0 ; k<8 ; k++){
        printf("%d ",A[k]);
    }
    printf("\n==================================\n");

    //quickSort(A,0,7);
    partition(A,0,1);

    for(k=0 ; k<8 ; k++){
        printf("%d ",A[k]);
    }
    printf("\n");

    return 0;
}
