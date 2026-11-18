class Solution {
    vector<vector<bool>> seen;
    string word;
public:
    bool find(int currIndex, int a, int b, vector<vector<char>>& board) {
        if (a < 0 || a >= board.size() || b < 0 || b >= board[0].size() || seen[a][b] || word[currIndex] != board[a][b]) {
            return false;
        }


        if (currIndex == word.length() - 1) {
            return true;
        }



        seen[a][b] = true;
        bool found = (find(currIndex + 1, a + 1, b, board) || 
                find(currIndex + 1, a - 1, b, board) ||
                find(currIndex + 1, a, b + 1, board) ||
                find(currIndex + 1, a, b - 1, board));
        seen[a][b] = false;
        return found;
    }

    bool exist(vector<vector<char>>& board, string word) {
        seen = vector(board.size(), vector<bool>(board[0].size(), false));
        this->word = word;

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == word[0]) {
                    if (find(0, i, j, board)) {
                        return true;
                    }
                }
            }
        }
        return false;

            
    }
};
