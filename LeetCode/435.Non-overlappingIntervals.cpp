#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
    public:
        int eraseOverlapIntervals(vector<vector<int>>& intervals) {
            int k;
            for_each(intervals.begin(),intervals.end(),[](vector<int> element){ 
                for_each(element.begin(),element.end(),[](int i){
                     cout << i << " "; 
                });    
            });
            //sort(intervals.begin(),intervals.end(),[](int element){ cout });
            return 0;   
            
        }   
};