/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
    vector<int> adjList[101];
    vector<bool> done;
    Node* nodeList[101];
public:
    void findAdj(Node* node) {
        if (!node or done[node->val]) return;
        int n=node->neighbors.size();
        for (int i=0; i<n; i++) adjList[node->val].push_back(node->neighbors[i]->val);
        done[node->val]=true;
        for (int i=0; i<n; i++) findAdj(node->neighbors[i]);
    }
    
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        done.assign(101, false);
        findAdj(node);
        /*int count=0;
        for (vector<int>& v:adjList){
            cout << count << "[";
            for (int &i:v) cout << i << " ";
            count++;
            cout << "]";
        }*/
        for (int i=0; i<101; i++){
            if (done[i]) nodeList[i]=new Node(i);
            else nodeList[i]=nullptr;
        }
        for (int i=0; i<101; i++){
            if (!done[i]) continue;
            for (int &adj:adjList[i]) nodeList[i]->neighbors.push_back(nodeList[adj]);
            done[i]=false;
        }
        return nodeList[node->val];
    }
};