#include <stdio.h>

int findKthLargest(int*, int, int);
void quickSelectSort(int*, int, int);

int main()
{
    int nums[6] = {1, 9, 3, 8, 5, 7};
    int k = 4;
    int ans;
    ans = findKthLargest(nums, 6, 4);
    printf("The Kth number of the array is: %d", ans);
    return 0;
}

int findKthLargest(int *nums, int numsSize, int k)
{
    quickSelectSort(nums, numsSize, k);
    return *(nums + k - 1);
}

void quickSelectSort(int *p, int numsSize, int k)
{
    int count = 0, tmp;
    int n = numsSize;
    int key = *(p + numsSize - 1);
    int *nums;
    nums = p;
    while (numsSize > 0)
    {
        if (*p <= key)
            count++;
        else
        {
            tmp = *p;
            *p = *(p - count);
            *(p - count) = tmp;
        }
        p++;
        numsSize--;
    }
    if (k <= n - count)
        quickSelectSort(nums, n - count, k);
    else
        quickSelectSort(nums + n - count, count, k - n + count);
}
