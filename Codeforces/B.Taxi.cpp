#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    int t, x, taxis = 0;
    cin >> t;
    vector<int> people(4, 0);
    for (int i = 0; i < t; i++)
    {
        cin >> x;
        people[x - 1]++;
    }
 
    // cout << "Antes\n";
 
    // for_each(people.begin(),people.end(),[](int i){cout << i << " ";});
    taxis = people[3];
    people[3] = 0;
    int min_group = min(people[2], people[0]);
 
    people[0] -= min_group;
    people[2] -= min_group;
    taxis += min_group;
    taxis += people[2];
    people[2] = 0;
 
    taxis += people[1] / 2;
    people[1] %= 2;
 
    if (people[1] != 0)
    {
        taxis++;
        people[0] -= min(2,people[0]);
    }
    
    if (people[0] != 0 && people[0] > 3)
    {
        taxis += people[0] / 4;
        people[0] %= 4;
        if (people[0] != 0)
            taxis++;
    }
    else if (people[0] != 0)
    {
        taxis++;
    }
    people[0] = 0;
 
    cout << taxis;
 
    return 0;
}