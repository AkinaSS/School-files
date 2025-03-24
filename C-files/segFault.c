#include <stdio.h>
#include <stdlib.h>

void foo(int *ptr, int size) {
    int arr[10];
    int i;
    for (i = 0; i<size; i++) {
        arr[i] = ptr[i];
    }
    return;
}

int main() {
    int *ptr = (int *)malloc(sizeof(int) * 20);
    foo(ptr, 20);
    printf("the value is %d\n", ptr[0]);
    return 0;
}