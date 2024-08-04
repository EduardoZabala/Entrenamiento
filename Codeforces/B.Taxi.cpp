#include <iostream>
#include <algorithm>
#include <cmath> 
using namespace std;
int main(){
    int t,acum=0,num;
    cin >> t ;
    for(int i = 0; i < t; i++){
        cin>>num;
        acum+=num;
    }
    if(acum%4!=0){
      t= (round(acum/4) + 1 );  
    }
    t = acum/4;
    cout << t; 
    return 0;
}
