#include <bits/stdc++.h>
using namespace std;
int main (){
    //variables
    int j=1,n,pos=0,even,odd;
    cin >> n ;
    vector<int>v(n);
    for(int i  = 0; i < n; i++ ){
        cin>>v[i];
    }
    
    for (int i = 0; i < n; i++){
        if(v[i]%2==0){
            even++;
        }else{
            odd++;
        }
    }
    if (even == 1){
        for (int i = 0; i < n; i++){
            if(v[i]%2==0){
                pos=i+1;
                break;
            }
        }
    }else{
        for (int i = 0; i < n; i++){
            if(v[i]%2!=0){
                pos=i+1;
                break;
            }
        }
    }
    
    cout << pos << endl;
    return 0;
}