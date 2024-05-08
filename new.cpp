#include <bits/stdc++.h>
using namespace std;

double f(double x)
{
    double ans = 0.2 + 25 * x - 200 * pow(x, 2) + 675 * pow(x, 3) - 900 * pow(x, 4) + 400 * pow(x, 5);
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

// Simpson's 1/3 rule
double simpson13(double a, double b, int n)
{
    double h = (b - a) / n;
    double sum = f(a) + f(b);
    for (int i = 1; i < n; i++)
    {
        double x = a + i * h;
        sum += (i % 2 == 0) ? 2 * f(x) : 4 * f(x);
    }
    return h * sum / 3;
}

// Simpson's 3/8 rule
double simpson38(double a, double b, int n)
{
    double h = (b - a) / (3 * n);
    double sum = f(a) + f(b);
    for (int i = 1; i < 3 * n; i++)
    {
        double x = a + i * h;
        sum += (i % 3 == 0) ? 2 * f(x) : 3 * f(x);
    }
    return 3 * h * sum / 8;
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
    double a = 0, b = 1; // Integration limits
    int n = 10;          // Number of intervals

    cout << "Simpson's 1/3 rule: " << simpson13(0, 0.8, 4) << endl;
    cout << "Simpson's 3/8 rule: " << simpson38(0, 0.8, 4) << endl;
    cout << trapezoid(0, 0.8, 4) << endl;

    return 0;
}