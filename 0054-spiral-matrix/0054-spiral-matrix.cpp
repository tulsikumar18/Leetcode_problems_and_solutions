class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        // find out  Row size and colm size 
        int row = matrix.size();
        int col = matrix[0].size();
        vector<int> temp;
        // Intialise all the Index value as you are printing
        int StartRow = 0;
        int Endcolm = col - 1;
        int EndRow = row - 1;
        int StartCol = 0;
        int total  = row * col;
        int count = 0;
        while(count < total)
        {
            for(int j = StartCol ; j <= Endcolm && count < total;j++)
            {
                temp.push_back(matrix[StartRow][j]);
                count++;
            }
            StartRow++;
            for(int j = StartRow; j <= EndRow  && count < total; j++)
            {
                temp.push_back(matrix[j][Endcolm]);
                count++;
            }
            Endcolm--;
            for(int j = Endcolm; j >= StartCol && count < total;  j--)
            {
                temp.push_back(matrix[EndRow][j]);
                count++;
            }
            EndRow--;
            for(int j = EndRow; j >= StartRow && count < total; j--)
            {
                temp.push_back(matrix[j][StartCol]);
                count++;
            }
            StartCol++;
            
        }
        return temp;
    }
};