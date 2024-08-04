#include <bits/stdc++.h>
#include <vector>
using namespace std;
int main (){
    //variables
    int coins,acum=0,total_twin,total_coins=0;
    cin >> coins ;
    vector<int>v (coins);
    for (int i = 0; i < coins; i++){
       cin >> v[i]; //pido los de una vez al acumulador
       total_twin+=v[i];
    }
    total_twin /= 2; //Varible que permite saber la mitad de las monedas
    // Ordena el array de mayor a menor
    sort(v.begin(), v.end(), greater<int>());
    acum=0;
    for(int i = 0 ; i < coins; i++){
        if (acum > total_twin){
            break;
        }else{
            acum+=v[i];
            total_coins++;
        }    
    }
    
    cout << total_coins<< endl;
    return 0;
}