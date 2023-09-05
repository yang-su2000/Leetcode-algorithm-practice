/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head==NULL) return NULL;
        Node* ptr=head;
        while (ptr) {
            Node* copy=new Node(ptr->val);
            copy->next=ptr->next;
            ptr->next=copy;
            ptr=copy->next;
        }
        ptr=head;
        while (ptr) {
            ptr->next->random=ptr->random ? ptr->random->next : NULL;
            ptr=ptr->next->next;
        }
        Node* _old=head;
        Node* _new=head->next;
        Node* newhead=head->next;
        while (_old) {
            _old->next=_old->next->next;
            _new->next=_new->next ? _new->next->next : NULL;
            _old=_old->next;
            _new=_new->next;
        }
        return newhead;
    }
};