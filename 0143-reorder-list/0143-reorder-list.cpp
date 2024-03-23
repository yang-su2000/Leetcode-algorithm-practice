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
    void reorderList(ListNode* head) {
        if (!head) return;
        vector<int> list;
        ListNode* cur=head;
        while (cur) {
            list.push_back(cur->val);
            cur=cur->next;
        }
        //for (int i:list) cout << i << " ";
        //cout << endl;
        int l=1, r=list.size()-1;
        bool left=false;
        ListNode* newhead=new ListNode();
        cur=newhead;
        while (l<=r) {
            if (left) {
                cur->next=new ListNode(list[l]);
                //cout << list[l] << " ";
                l++;
                left=false;
            } else {
                cur->next=new ListNode(list[r]);
                //cout << list[r] << " ";
                r--;
                left=true;
            }
            cur=cur->next;
        }
        head->next=newhead->next;
    }
};