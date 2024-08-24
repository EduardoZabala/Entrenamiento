#include <iostream>
#include <vector>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t, n, cont, spell;
    cin >> t;
    for (int j = 0; j < t; j++)
    {
        cin >> n;
        cont = 0, spell = 0;
        vector<int> vec(n);
        for (int i = 0; i < n; i++)
            cin >> vec[i];
        for (int i = 0; i < n; i++)
        {
            if (vec[i] == 1)
            {
                cont++;
            }
        }

        if (cont % 2 != 0)
        {
            spell = cont / 2 + 1;
        }
        else
        {
            spell = cont / 2;
        }

        n -= cont;
        spell += n;
        cout << spell << "\n";
    }
    return 0;
}