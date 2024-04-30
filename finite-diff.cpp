#include <bits/stdc++.h>
using namespace std;

double timeSteps = 5000;
double dx = 0.02;
double dt = 0.1;
double pi = atan(1) * 4.0;
double alpha = 20;
double x0 = -0.5;
double p0 = 50;
double m = 14500;
double xmin = -2.0;
complex<double> ii(0, 1);
double V(double x)
{

    if (x < 0)
        return 0;
    return 0.1;
}
complex<double> psi(double x)
{

    complex<double> temp(2 * alpha, 0);
    temp /= pi;
    temp = sqrt(temp);
    temp = sqrt(temp);
    complex<double> ok(0, p0 * (x - x0));
    temp *= exp(-alpha * (x - x0) * (x - x0)) * exp(ok);
    return temp;
}
complex<double> arr[5002][258];
int main()
{

    // ofstream outfile("q1.txt");
    cout << fixed << endl;
    cout << setprecision(11);
    for (int x = 0; x <= 256; x++)
    {
        arr[0][x] = psi(xmin + x * dx);
    }

    for (int x = 0; x <= 256; x++)
    {

        if (x == 0)
        {
            arr[1][x] = arr[0][x] + ii * dt * (((1.0) / (2.0 * m)) * ((arr[0][x] - 2.0 * arr[0][x + 1] + arr[0][x + 2]) / (dx * dx)) - V(xmin + x * dx) * arr[0][x]);
        }
        else if (x == 256)
        {
            arr[1][x] = arr[0][x] + ii * dt * (((1.0) / (2.0 * m)) * ((arr[0][x] - 2.0 * arr[0][x - 1] + arr[0][x - 2]) / (dx * dx)) - V(xmin + x * dx) * arr[0][x]);
        }
        else
        {
            arr[1][x] = arr[0][x] + ii * dt * (((1.0) / (2.0 * m)) * ((arr[0][x + 1] - 2.0 * arr[0][x] + arr[0][x - 1]) / (dx * dx)) - V(xmin + x * dx) * arr[0][x]);
        }
    }

    for (int t = 2; t <= 5000; t++)
    {

        for (int x = 0; x <= 256; x++)
        {
            int i = t;
            if (x == 0)
            {
                arr[i][x] = arr[i - 2][x] + (2.0 * ii * dt) * ((1.0 / (2.0 * m)) * ((arr[i - 1][x] - 2.0 * arr[i - 1][x + 1] + arr[i - 1][x + 2]) / (dx * dx)) - V(xmin + x * dx) * arr[i - 1][x]);
            }
            else if (x == 256)
            {
                arr[i][x] = arr[i - 2][x] + (2.0 * ii * dt) * ((1.0 / (2.0 * m)) * ((arr[i - 1][x] - 2.0 * arr[i - 1][x - 1] + arr[i - 1][x - 2]) / (dx * dx)) - V(xmin + x * dx) * arr[i - 1][x]);
            }
            else
            {

                arr[i][x] = arr[i - 2][x] + (2.0 * ii * dt) * ((1.0 / (2.0 * m)) * ((arr[i - 1][x + 1] + arr[i - 1][x - 1] - 2.0 * arr[i - 1][x]) / (dx * dx)) - V(xmin + x * dx) * arr[i - 1][x]);
            }
        }
    }
    ofstream output("2500.txt");
    for (int x = 0; x <= 256; x++)
    {

        // auto vv = norm(arr[1500][x]);
        output << x << "\t" << norm(arr[2500][x]) << endl;

        // cout<<xmin+x*dx<<endl;
        // cout << xmin + x * dx << " " << norm(arr[500][x]) << endl;
    }
    output.close();
}