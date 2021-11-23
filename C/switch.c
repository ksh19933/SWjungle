#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void){
  srand(time(NULL));
  int i = rand() % 3;
  switch(i){
    case (0):
      printf("rock \n");
      break;
    case (1):
      printf("paper \n");
      break;
    case (2):
      printf("scissor \n");
      break;
    }
  return 0;
}