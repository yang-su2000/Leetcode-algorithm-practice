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
    ListNode* reverseList(ListNode* head) {
        ListNode* cur=NULL;
        ListNode* top;
        while (head) {
            top=new ListNode(head->val);
            top->next=cur;
            cur=top;
            head=head->next;
        }
        return cur;
    }
};