#include <stdio.h>
#include <string.h>

int main () {
    printf("Write, compile, and run a program in C to print the even numbers from 0 to N\n");
	int i;
    for (i = 0; i <= 99; i++) 
	{
		if(i%2 == 0)
		{
		  printf("%d", i);
		  printf("\n");
		}
	}
	return 0;
    
}