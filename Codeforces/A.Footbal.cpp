#include<iostream>
#include<vector>
using namespace std;
int main(){
    string s;
    int count=0;
    char pivot;

    
    cin >> s;
    pivot=s[0];
    for(int i = 1;i < s.length();i++ ){
        if(count>=6){
            break;
        }
    
        if (pivot==s[i])
        {
            count++;
        }else{
            pivot=s[i];
            count=0;
        }
    }  
    if(count>=6){
        cout<<"YES";
    }else{
        cout<<"NO";
    }
    return 0;
}