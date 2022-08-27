#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x, y, i, j;
    for (x = 0; x <= 5; x++)
    {
        for (y = 0; y <= 5; y++)
        {
            for (i = 0; i <= 5; i++)
            {
                for (j = 0; j <= 5; j++)
                {
                    if (x > y || i > 0 && j < 5)
                    {
                        cout << x << y << i << j << endl;
                    }
                }
            }
        }
    }

    return 0;
}