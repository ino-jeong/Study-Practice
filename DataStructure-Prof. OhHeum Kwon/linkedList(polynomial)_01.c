#include <stdio.h>
#include <stdlib.h>
#define MAX_POLYS 100


typedef struct term {
    int coef;
    int expo;
    struct term *next;
} Term;

typedef struct polynomial{
    char name;
    Term * first;
    int size;//=0;
} Polynomial;

Polynomial *polys[MAX_POLYS];
int n=0;

Term *create_term_instance();
Polynomial *create_polynomial_instance(char name);
void add_term(int c, int e, Polynomial *poly);


int main()
{
    printf("Hello, World!\n");

    return 0;
}



Term *create_term_instance(){
    Term *t = (Term *)malloc(sizeof(Term));
    t->coef = 0;
    t->expo = 0;
    return t;
}

Polynomial *create_polynomial_instance(char name){
    Polynomial *ptr_poly = (Polynomial *)malloc(sizeof(Polynomial));
    ptr_poly->name = name;
    ptr_poly->size = 0;
    ptr_poly->first = NULL;
    return ptr_poly;
}

void add_term(int c, int e, Polynomial *poly){
  if(c==0){ // coefficient = 0 -> 0
      return;
  } 
  Term *p = poly->first;
  Term *q = NULL;
  
  while(p!=NULL && p->expo>e){
      q=p;
      p=p->next;
  }
  
  //if there exists same exp. term.
  if(p!=NULL && p->expo==e){
      p->coef +=c;
      
      if(p->coef == 0){
          if(q==NULL){ //this term is first term
              poly->fist = p->next;
          }
          else{
              q->next = p->next;
          }
          poly->size--;
          free(p); //check whether following terms should be freed or not.
      }
      return;
  }
  
  //there is no same exp. term. create new one.
  Term *term = create_term_instance();
  term->coef = c;
  term->expo = e;
  
  //if new term is first term.
  if(q==NULL){
      term->next=p;
      poly->fist=term;
  }
  else{
      term->next=p
      q->next=term;
  }
  poly->size++;
  
}

