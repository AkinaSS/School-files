#include <stdio.h>

void print_array(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d\n", arr[i]);
    }
}
int main () {
int some[5], more[10], i;

for (i = 0; i < 5; i++) {  // initialize the first 5 elements of both arrays
    some[i] = i * i;
    more[i] = some[i];
}

for (i = 5; i < 10; i++) { // initialize the last 5 elements of "more" array
    more[i] = more[i-1] + more[i-2];
}

printf("\n");
print_array(some, 5);    // prints all 5 values of "some"
printf("\n");
print_array(more, 10);   // prints all 10 values of "more"
printf("\n");
print_array(more, 8);    // prints just the first 8 values of "more"
}
