
#include <bits/stdc++.h>
using namespace std;

double f(double x)
{
    return (exp(x) - x - 2);
}
double g(double x)
{
    return (exp(x) - 2);
}
double diff(double x)
{
    double h = 0.000001;
    double ans = (f(x + h) - 2 * f(x) + f(x - h)) / (h * h);
    return ans;
}
double newton(double x)
{
    double x0 = x;
    while (fabs(f(x0)) > 0.000001)
    {
        double x_new = x0 - (f(x0) / diff(x0));
        x0 = x_new;
    }
    return x0;
}
double secant(double a, double b)
{

    double x0 = a;
    double x1 = b;

    while (fabs(f(x1)) > 0.000001)
    {
        double x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0));
        x0 = x1;
        x1 = x_new;
    }
    return x1;
}
double bisection(double low, double high)
{
    double mid;
    do
    {
        mid = (high + low) / 2;
        if (f(mid) * f(high) < 0)
            low = mid;
        else if (f(mid) * f(low) < 0)
            high = mid;
    } while (fabs(f(mid)) > 0.000001);

    return mid;
}
double false_position(double low, double high)
{
    double mid;
    do
    {
        mid = (f(high) * low - f(low) * high) / (f(high) - f(low));
        if (f(mid) * f(low) < 0)
            high = mid;
        else if (f(mid) * f(high) < 0)
            low = mid;
    } while (abs(f(mid)) > 0.000001);

    return mid;
}
double fixed_point(double x)
{
    double x0 = x;
    double x1 = g(x);
    while (fabs(x1 - x0) > 0.000001)
    {
        double x_new = g(x1);
        x0 = x1;
        x1 = x_new;
    }
    return x1;
}

int main()
{

    cout << secant(1.5, 2) << endl;
    cout << newton(1) << endl;
    cout << bisection(0, 2) << endl;
    cout << false_position(0, 2) << endl;
    cout << fixed_point(1) << endl;

    return 0;
}