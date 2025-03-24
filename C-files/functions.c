#include <stdio.h>

/* max: computes the larger of two integer values
 *   x: one integer value
 *   y: the other integer value
 *   returns: the larger of x and y
 */

    int max(int x, int y) {
    int bigger;

    bigger = x;
    if (y > x) {
        bigger = y;
    }
    printf("  in max, before return x: %d y: %d\n", x, y);
    return bigger;
    }
int main () {
    int val1, val2;
    int result;
    val1 = 10;
    val2 = 100;

    result = max(val1, val2);
    printf("\tthe bigest number is %d\n", result);
}
