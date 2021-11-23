#include <stdio.h>

int main(void){
  // for (int i = 0; i <= 10; i++)
  // {
  //   printf("Hello World\n");
  // }
  int i = 0;
  while (i < 1)
  {
    printf("Hello while, %d\n", i++);
  }
  i = 0; 
  do
  {
    printf("Hello dowhile, %d\n", i++);
  } while (i < 1);
  return 0;
}