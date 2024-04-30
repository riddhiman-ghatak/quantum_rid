#include <bits/stdc++.h>
using namespace std;

double f(double x)
{
    double ans = 1 / (1 + 16 * x * x);
    return ans;
}
double transform(double x)
{
    double ans = (2 * x - (-5 + 5)) / (5 + 5);
    return ans;
}

vector<double> chebyshev_nodes(double n)
{
    vector<double> cheb_nodes(n);
    for (int i = 0; i < n; i++)
    {
        cheb_nodes[i] = cos((2 * i + 1) * M_PI / (2 * n));
    }
    return cheb_nodes;
}

double cheb_Ts(double n, double x)
{
    return cos(n * acos(x));
}

vector<double> cheb_coeff(double n)
{
    vector<double> cheb_coff(n);
    vector<double> cheb_node = chebyshev_nodes(n);
    for (int i = 0; i < n; i++)
    {
        cheb_coff[0] += f(cheb_node[i]);
    }
    cheb_coff[0] /= n;

    for (int j = 1; j < n; j++)
    {
        for (int k = 0; k < n; k++)
        {
            cheb_coff[j] += f(cheb_node[k]) * cos(j * M_PI * (2 * k + 1) / (2 * n));
        }
        cheb_coff[j] = 2 * cheb_coff[j] / n;
    }
    return cheb_coff;
}

double cheb_poly(double n, double x)
{
    vector<double> c = cheb_coeff(n);
    double ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans += c[i] * cheb_Ts(i, x);
    }
    return ans;
}

double newtonInterpolation(double x, const vector<double> &xValues, const vector<double> &yValues)
{
    int n = xValues.size();
    vector<vector<double>> a(n, vector<double>(n, 0.0));

    for (int i = 0; i < n; ++i)
        a[i][0] = yValues[i];

    for (int j = 1; j < n; ++j)
    {
        for (int i = 0; i < n - j; ++i)
        {
            a[i][j] = (a[i + 1][j - 1] - a[i][j - 1]) / (xValues[i + j] - xValues[i]);
        }
    }

    double result = a[0][0];
    double term = 1.0;

    for (int j = 1; j < n; ++j)
    {
        term *= (x - xValues[j - 1]);
        result += term * a[0][j];
    }

    return result;
}
double lagrange_interpolation(vector<double> &x_values, vector<double> &y_values, double x)
{
    int n = x_values.size();
    double result = 0.0;

    for (int i = 0; i < n; ++i)
    {
        double term = y_values[i];
        for (int j = 0; j < n; ++j)
        {
            if (i != j)
            {
                term *= (x - x_values[j]) / (x_values[i] - x_values[j]);
            }
        }
        result += term;
    }

    return result;
}

int main()
{
    double n = 20;
    double x = 1.2;
    double trans = transform(x);
    cout << cheb_poly(20, trans);

    return 0;
}