//https://atcoder.jp/contests/abc172/tasks/abc172_d

#include <iostream>
using namespace std;
int main(void)
{
    long long n, count = 0, sumA = 0, i = 0;
    cin >> n;
    while (i < n)
    {
        sumA = (i + 1) * (n / (i + 1) + 1) * (n / (i + 1)) / 2;
        count += sumA;
        i++;
    }
    cout << count;
}