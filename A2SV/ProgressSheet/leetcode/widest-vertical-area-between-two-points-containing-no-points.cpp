class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> point(points.size());
        for (int i=0; i < points.size(); i++){
            point[i] = points[i][0];
        }
        sort(point.begin(), point.end());
        int m = 0;
        for (int i=1; i < point.size(); i++){
            m = max(m, (point[i] - point[i-1]));
        }
        return m;
    }
};