#include <iostream>
#include <vector>
#include <algorithm> //incluye la funcion sort
#include <set>
using namespace std;
set<int> FindWinners( vector<vector<int>>&Matches){
    set<int>aux;
    for(auto i : Matches){
        aux.insert(i[0]);
    }
    return aux;
}
vector<int> FindLost( vector<vector<int>>&Matches){
    vector<int>aux;
    for(auto i : Matches){
        aux.push_back(i[1]);
    }
    return aux;
}
/* Esta es una manera de resolver el ejercicio hasta el caso 124,
   tenemos que intentar encontrar una manera mas optima*/
int main (){
    //variables
    vector<vector<int>>Matches= {{1,3},{2,3},{3,6},{5,6},{5,7},{4,5},{4,8},{4,9},{10,4},{10,9}};
    set<int>Winners; // 1 2 3 5 5 4 4 4 10 10 
    vector<int>lost; // 3 3 6 6 7 5 8 9 4 9  
    vector<vector<int>>Answer(2);
    Winners=FindWinners(Matches);
    lost=FindLost(Matches);
    int t = int(lost.size());
    bool sw;
    vector<int>aux;
    //Validar si algun elemento de winners esta en lost   
    for(int i : Winners) if (find(lost.begin(),lost.end(),i)==lost.end()) Answer[0].push_back(i); 
    //
    for(int i = 0; i < t ; i++){
        sw=false;
        for(int j = 0;j < t;j++){
            if(lost[i]==lost[j] && i!=j){
                sw=true;
            }
        }
        if(sw==false){
            aux.push_back(lost[i]);
        }
    }
    sort(aux.begin(),aux.end());
    for(int i : aux) Answer[1].push_back(i);
    for(int i : Answer[1]) cout << i << " ";
    return 0;
    
}