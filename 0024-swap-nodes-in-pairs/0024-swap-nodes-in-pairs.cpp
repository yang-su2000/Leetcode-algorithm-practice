/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (not head) return head;
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* cur = dummy;
        ListNode* cur2;
        while (cur->next and cur->next->next) {
            cur2 = cur->next->next;
            cur->next->next = cur2->next;
            cur2->next = cur->next;
            cur->next = cur2;
            cur = cur->next->next;
        }
        return dummy->next;
    }
};