#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// ******* Aprendiendo a usar Lambda *********

class Lambda{
    public:
        void Show(){
                vector<string>prueba = {"Esto","es","una","prueba"};
                auto print = [](string elemento){// Crea una variable que tiene una funcion
                    for_each(elemento.begin(),elemento.end(),[](char e){cout << e << " ";});
                            //Apuntador inicio -Apuntador fin
                };
                for_each(prueba.begin(),prueba.end(),[=](string elemento){print(elemento);cout << endl; });
                                                    // [] -> Sin Contexto
                                                    // [=] -> Contexto por copia
                                                    // [&] -> Contexto por referencia
            }

};
class Lambda2{

    public:
        void Show(){
        vector<int>numbers = {1,2,3,5};
        auto print = [](auto i){cout << i << " ";};
        for_each(numbers.begin(),numbers.end(),[](int &n){n*=2;}); 
                                                    //Parametro con Referencia
        for_each(numbers.begin(),numbers.end(),[=](int i){print(i);}); 
                                              //Contexto Copia
        }
};
int main(){

    Lambda2 la;
    la.Show();
    return 0;
}

