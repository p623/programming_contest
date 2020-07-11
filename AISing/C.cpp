#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
int main(void)
{
    long long n, top, count, i = 0, x = 0, y = 0, z = 0;
    cin >> n;
    while (i < n)
    {
        top = sqrt(i);
        count = 0;
        x = 0;
        while (x < top - 1) {
            y = 0;
            while (y < x+1) {
                z = 0;
                while (z < y+1) {
                    if ((x+1)*(x+1) + (y+1)*(y+1) + (z+1)*(z+1) + (x+1)*(y+1) + (y+1)*(z+1) + (z+1)*(x+1) == i+1) {
                        if (x+1 == y+1 and y+1 == z+1) {
                            count += 1;
                        } else if (x+1 != y+1 and y+1 != z+1 and z+1 != x+1) {
                            count += 6;
                        } else {
                            count += 3;
                        }
                        
                    }
                    z++;
                }
                y++;
            }
            x++;
        }
        cout << count << endl;
        i++;
    }
}