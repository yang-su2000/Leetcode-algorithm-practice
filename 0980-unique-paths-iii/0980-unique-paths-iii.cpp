class Solution {
    int nr;
    int nc;
    int tar_d=2;
    int ans=0;
    const vector<vector<int>> dir{{1,0},{0,1},{-1,0},{0,-1}};
public:
    void dfs(int i, int j, int visited, vector<vector<int>>& grid) {
        for (auto &d:dir) {
            int nei=i+d[0];
            int nej=j+d[1];
            if (nei<0 or nei>=nr or nej<0 or nej>=nc) continue;
            int det=grid[nei][nej];
            if (det==2) {
                if (visited+1==tar_d) ans++;
            } else if (det==0) {
                grid[nei][nej]=-1;
                dfs(nei, nej, visited+1, grid);
                grid[nei][nej]=0;
            }
        }
    }
    
    int uniquePathsIII(vector<vector<int>>& grid) {
        nr=grid.size();
        nc=grid[0].size();
        int si, sj;
        for (int i=0; i<nr; i++)
            for (int j=0; j<nc; j++){
                if (grid[i][j]==1) {si=i,sj=j;} 
                else if (grid[i][j]==0) tar_d++;
            }
        dfs(si, sj, 1, grid);
        return ans;
    }
};