#include<iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,k,ans;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        cin >> k;
        int a[k];
        for (int j = 0; j < k; j++) cin>> a[j];
        ans=0;
        for (int j = 0; j < k-1; j++) if(a[j]>a[j+1] && a[j]>ans )ans=a[j]; 
        cout << ans << "\n";
    }
    return 0;
}