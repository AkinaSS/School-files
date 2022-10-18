#include <stdio.h>

int main() {
    int num, val;
    int i;

    printf("Enter a value: ");
    scanf("%d", &num);
    // make sure num is not negative
    if (num < 0) {
        num = -num;
    }
    else if (num == 0) {
        i = 0;
        while (i < 10) {
        printf("i is %d\n", i++);  // i++: increment i's value after using it
        }
    }
    val = 1;
    while (val < num) {
        printf("%d\n", val);
        val = val * 2;
    }
    
    
    //printf(val);

    

    return 0;
}