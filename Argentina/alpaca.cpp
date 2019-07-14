#include <iostream>

using namespace std;

long long get_pisano_period(long long m) {
    long long a = 0, b = 1, c = a * 2 + b;
    for (int i = 0; i < m * m; i++) {
        c = (a * 2 + b) % m;
        a = b;
        b = c;
        if (a == 0 && b == 1) return i + 1;
    }
}

long long get_jacobsthal_huge(long long n, long long m) {
    long long remainder = n % get_pisano_period(m);

    long long first = 0;
    long long second = 1;

    long long res = remainder;

    for (int i = 1; i < remainder; i++) {
        res = (first * 2 + second) % m;
        first = second;
        second = res;
    }

    return res % m;
}

int main() {
    long long n = 234612846789230;
    long long m = 123456789;
    
    cout << get_jacobsthal_huge(n, m) << endl;
}