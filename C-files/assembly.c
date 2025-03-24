 #include <stdio.h>
 #include <stdlib.h>
 
 int add2(int a){
    return a + 2;}
      
      int main(){
         int x = 10;
         x = add2(x);
         printf("x is %d\n", x);
         return 0;
      }