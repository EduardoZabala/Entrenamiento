#include<iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string field;
    int n,j,k,screw;
    cin>>n;
    for (int i = 0; i < n ;i++){
        cin >> k;
        cin >> field;
        screw = 0;
        j=0;   
        while(j <= field.length()){//**#*
            if(field[j]=='.'){
                screw++;
                j+=3;
            }else{
                j++;
            }
        }
        cout << "Case "<<to_string(i+1)<<": "<<screw << "\n"; //2
    }
    return 0;
}