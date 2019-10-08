/*
 * @lc app=leetcode.cn id=215 lang=c
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start


int findKthLargest(int* nums, int numsSize, int k){
    int key;
    while(numsSize > 0){
        numsSize--;

    }
    return *nums + 3;
}


void quicksort(int *nums, int numsSize){
    int key, i, count;
    int *slide;
    i = 0;
    count = 0;
    key = *nums + numsSize - 1;
    while(i < numsSize-1){
        if(*nums+i >= key){
            swap(*nums, *nums-count);
        }
        else{
            count++;
        }
        i++;
    }
    quicksort(*nums, numsSize - count);
    quicksort(*nums + numsSize - count, count);
    return;
}


// @lc code=end

