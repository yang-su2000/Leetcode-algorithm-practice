struct Node
{
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    int key;
    int val;
    Node* prev;
    Node* next;
};
class Solution
{
public:
    /**
     * lru design
     * @param operators int整型vector<vector<>> the ops
     * @param k int整型 the k
     * @return int整型vector
     */
    unordered_map<int, Node*> M;
    Node* Head = nullptr;
    Node* Tail = nullptr;
    int cap = 0;
    
    void add(int k, int v) {
        Node* newHead = new Node(k, v);
        M[k] = newHead;
        newHead->next = Head;
        if (Head) Head->prev = newHead;
        else Tail = newHead;
        Head = newHead;
    }
    
    void remove(Node* toRemove) {
        if (!toRemove) return;
        Node* pre = toRemove->prev;
        Node* nex = toRemove->next;
        if (toRemove == Tail) Tail = pre;
        if (toRemove == Head) Head = nex;
        delete toRemove;
        toRemove = nullptr;
        if (pre) pre->next = nex;
        if (nex) nex->prev = pre;
    }
    
    vector<int> LRU(vector<vector<int>> &operators, int k) {
        vector<int> ret;
        for (auto &v:operators) {
            if (v[0] == 1) {
                if (M.count(v[1])) {
                    remove(M[v[1]]);
                    add(v[1], v[2]);
                } else {
                    add(v[1], v[2]);
                    cap++;
                    if (cap > k) {
                        int x = Tail->key;
                        remove(Tail);
                        M.erase(x);
                        cap--;
                    }
                }
            } else {
                if (!M.count(v[1])) ret.emplace_back(-1);
                else {
                    int y = M[v[1]]->val;
                    remove(M[v[1]]);
                    add(v[1], y);
                    ret.emplace_back(y);
                }
            }
        for (auto &p:M) {
            delete(p.second);
            p.second = nullptr;
        }
        return ret;
    }
};