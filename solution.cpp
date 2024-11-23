class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m =box.size(),n=box[0].size();
        for(auto &row:box){
            int obstacle = row.size();
            for(int i = row.size()-1; i>=0; i--){
                if(row[i]=='#'){
                    char temp = row[i];
                    row[i]='.';
                    row[obstacle-1]=temp;
                    obstacle--;
                }

                if(row[i]=='*')
                    obstacle =i;
            }
        }

        vector<vector<char>>result(n,vector<char>(m,'.'));

        for(int i = 0; i<m; i++)
            for(int j = 0; j<n; j++)
                result[j][m-1-i] = box[i][j];
        
        return result;
    }
};