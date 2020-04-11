/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int offset = 0;
        ListNode res = l1;
        ListNode flag = l1;
        while (l1 != null && l2 != null) {
            int sum = l1.val + l2.val + offset;
            l1.val = sum % 10;
            offset = sum / 10;

            flag = l1;
            l1 = l1.next;
            l2 = l2.next;
        }
        if (l2 != null) {
            flag.next = l2;
            l1 = l2;
        }
        while (offset > 0) {
            if (l1 == null) {
                flag.next = new ListNode(0);
                l1 = flag.next;
            }
            int sum = l1.val + offset;
            l1.val = sum % 10;
            offset = sum / 10;

            flag = l1;
            l1 = l1.next;
        }

        return res;
    }
}
// @lc code=end

