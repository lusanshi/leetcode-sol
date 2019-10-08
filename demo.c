#include <stdio.h>

int main(){
    int array[6] = {1, 2, 3, 4, 5, 6};
    int *index;
    index = array;
    printf("array[6]=%d", *index+5);
    return 0;
}
