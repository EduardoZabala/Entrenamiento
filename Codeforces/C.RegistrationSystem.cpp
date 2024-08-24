#include<iostream>
#include<unordered_map>
using namespace std;
int main(){
    unordered_map<string,int>Login;
    int k,count=0;
    string s;
    //LLenando el Login
    cin >> k;
    for(int i = 0 ; i < k;i++){
        cin>>s;
        if(Login.find(s)!=Login.end()){
            count = ++Login[s];
            Login[s+to_string(count)]=0;
            
            cout<<s+to_string(count)<<endl;
        }else{
            Login[s]=0;
            cout<<"OK"<<endl;
        }
    }
    return 0;
}