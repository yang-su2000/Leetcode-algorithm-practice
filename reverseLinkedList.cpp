/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode* cur=nullptr;
        ListNode* neHead=nullptr;
        while (pHead){
            neHead=pHead->next; // the real head
            pHead->next=cur; // make pHead as the next cur
            cur=pHead; // update cur to the next cur
            pHead=neHead; // make pHead the real head again
        }
        return cur;
    }
};