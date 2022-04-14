#include "stdlib.h"
#include "assert.h"
#define SIZE (1024*1024)
#define ITERS (1024)

int add(int * a, int  * b, int * c) {
  for (int i = 0; i < SIZE; i++) {
    a[i] = b[i] + c[i];
  }
  return 0;
}

int main() {
  int *a, *b, *c;
  a = (int *) malloc(sizeof(int)*SIZE);
  b = (int *) malloc(sizeof(int)*SIZE);
  c = (int *) malloc(sizeof(int)*SIZE);
  
  for (int i = 0; i < SIZE; i++) {
    b[i] = c[i] = i;
  }
  

  for (int i = 0; i < ITERS; i++) {
    add(a,b,c);
  }

  for (int i = 0; i < SIZE; i++) {
    assert(a[i] == i+i);
  }

}
