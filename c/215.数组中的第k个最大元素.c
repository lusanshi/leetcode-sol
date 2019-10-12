/*
 * @lc app=leetcode.cn id=215 lang=c
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start

int findKthLargest(int *nums, int numsSize, int k)
{
    /*
    int *bubble;
    int tmp, i, max;
    while(k > 0){
        k--;
        bubble = nums;
        for(i = 1; i < numsSize; i++){
            bubble++;
            if(*bubble < *(bubble-1)){
                tmp = *(bubble - 1);
                *(bubble - 1) = *bubble;
                *bubble = tmp;
            }
        }
        max = *bubble;
        numsSize--;
    }
    return max;
    */
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
        if (*p < key)
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

    if (k == n - count || n <= 2)
        return;
    else if (k < n - count)
        quickSelectSort(nums, n - count - 1, k);
    else
        quickSelectSort(nums + n - count, count, k - n + count);
}

// @lc code=end
