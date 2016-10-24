#include <stdio.h>

int A[8]={5,7,8,1,-10,99,1092,0};

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

void mergeSort(int* A, int p, int r){
    if(p<r){
        int q=(p+r)/2;
        
        mergeSort(A,p,q);
        mergeSort(A,q+1,r);
        merge(A,p,q,r);
    }
}

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
