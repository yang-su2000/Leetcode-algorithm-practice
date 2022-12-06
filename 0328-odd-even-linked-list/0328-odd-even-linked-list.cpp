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
    ListNode* oddEvenList(ListNode* head) {
        if (!head or !head->next) return head;
        ListNode* head1=new ListNode();
        head1->next=head;
        ListNode* head2=new ListNode();
        head2->next=head->next;
        ListNode* n1=head1->next;
        ListNode* n2=head2->next;
        while (n1->next and n2->next){
            n1->next=n2->next;
            n1=n1->next;
            n2->next=n1->next;
            n2=n2->next;
        }
        n1->next=head2->next;
        return head;
    }
};