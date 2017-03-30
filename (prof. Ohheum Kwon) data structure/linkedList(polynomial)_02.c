//calculate polynomial
int eval(Polynomial *poly, int x){
  int result = 0;
  Term *t = poly->first;
  
  while(t != NULL){
    result += eval_term(t, x);
    t = t->next;
  }
}



//calculater each term
int eval_term(Term *term, int x){
  int result = term->coef;
  int i=0;
  for(i=0; i<(term->expo); i++){
    result *=x;
  }
  return result;
}



//print polynomial
void print_poly(Polynomial *p){
  printf("%c=", p->name);
  Term *t = p->first;
  
  while(t!=NULL){
    print_term(t);
    printf("+");
    t=t->next;
  }
}



//print term
void print_term(Term *pTerm){
  printf("%dx^%d",pTerm->coef, pTerm->expo);
}

