#include <bits/stdc++.h>
using namespace std;

// sir I am Riddhiman.I have submitted already 2 days ago.
// But my file name was not in format , so I am submitting again

double f(double x)
{
    double ans = 2000 * log(140000 / (140000 - 2100 * x)) - 9.8 * x;
    return ans;
}
double trapezoid(double a, double b, int n)
{
    double term = 0;
    double h = (b - a) / n;
    for (int i = 1; i <= n - 1; i++)
    {
        term += f(a + i * h);
    }
    double ans = h * (f(a) / 2 + f(b) / 2 + term);
    return ans;
}
double romberg(int j, int k, double a, double b)
{
    int n = max(j + 1, k);
    vector<vector<double>> matrix(n + 1, vector<double>(n + 1, 0));

    for (int i = 1; i <= n; i++)
    {
        matrix[i][1] = trapezoid(a, b, pow(2, i - 1));
    }
    for (int col = 2; col <= n; col++)
    {
        for (int row = 1; row <= n - col + 1; row++)
        {
            matrix[row][col] = (pow(4, col - 1) * matrix[row + 1][col - 1] - matrix[row][col - 1]) / (pow(4, col - 1) - 1);
        }
    }

    return matrix[j][k];
}

int main()
{

    cout << romberg(1, 4, 8, 30) << endl;
    // cout << trapezoid(8, 30, 2) << endl;

    return 0;
}