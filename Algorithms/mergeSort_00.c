/****************************************************************
Merge sort practice.
Unsorted array input by user is not impemented yet.
Thus only for hard corded array A will be sorted and displayed.
****************************************************************/
#include <stdio.h>

//specified array for public
int A[8]={5,7,8,1,-10,99,1092,0}; 

//merge function
void merge(int* A, int p, int q, int r){
    
    int i=p, j=q+1, k=p;
    int temp[8];
    
    while(i<=q && j<=r){
        if( *(A+i) <= *(A+j) ){
            *(temp+k)=*(A+i);
            i++;
            k++;
        }
        else{
            *(temp+k)=*(A+j);
            j++;
            k++;
        }
    }
    
    while(i<=q){
        *(temp+k)=*(A+i);
        i++;
        k++;
    }
    
    while(j<=r){
        *(temp+k)=*(A+j);
        j++;
        k++;
    }
    
    for(i=p ; i<=r ; i++){
        *(A+i)=*(temp+i);
    }
    
}

//mergesort function. This function will call merge() for its process.
void mergeSort(int* A, int p, int r){
    if(p<r){
        int q=(p+r)/2;
        
        mergeSort(A,p,q);
        mergeSort(A,q+1,r);
        merge(A,p,q,r);
    }
}

//main
int main()
{
    int a=0;
    
    mergeSort(A,0,7);
    
    for(a=0;a<8;a++){
        printf("%d ",*(A+a));  
    }
    
    printf("\n");

    return 0;
}
