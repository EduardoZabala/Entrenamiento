#include <iostream>
#include<algorithm>
using namespace std;
int main(){
    int t,m,n,k;
    string c;
    cin >> t;
    for (int i = 0; i < t; i++){
        cin>>m;
        cin>>n;
        cin>>k;
        char a[m];
        char b[n];
        c = "";
        for (int i = 0; i < m; i++) cin >> a[i];
        for (int i = 0; i < n; i++) cin >> b[i];
        sort(a,a+m);//organizo los arreglos
        sort(b,b+n);//organizo los arreglos
        if(a[0]<b[0]){
           for(int i = 0; i < m ; i++){
                
           } 
        }

        
    }
   
    return 0;
}