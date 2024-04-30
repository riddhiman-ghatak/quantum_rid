#include <bits/stdc++.h>
using namespace std;

const double h_bar = 1;
const double m = 1;
const double dx = 0.01;

double v(double x)
{
    if (x <= 4.5)
    {
        return 4.5 * exp(-pow((x - 4.5) / 0.6, 2));
    }
    else
    {
        return 5 * exp(-(pow((x - 4.5) / 0.6, 2))) + 4;
    }
}

vector<complex<double>> schorindger(double E)
{
    int N = static_cast<int>(10 / dx);
    vector<complex<double>> psi(N, complex<double>(0, 0));
    double k = sqrt(2 * m * (E - v(0)) / pow(h_bar, 2));

    psi[0] = complex<double>(1, 0);
    psi[1] = exp(complex<double>(0, -k * dx));

    for (int j = 1; j < N - 1; j++)
    {
        psi[j + 1] = (2 - 2 * m * (E - v(j * dx)) * pow(dx, 2) / pow(h_bar, 2)) * psi[j] - psi[j - 1];
    }
    return psi;
}

double quantum_probability(double E)
{
    auto psi = schorindger(E);
    double mini = abs(psi[600]);
    double maxi = abs(psi[600]);
    for (int i = 601; i < psi.size(); i++)
    {
        mini = min(mini, abs(psi[i]));
        maxi = max(maxi, abs(psi[i]));
    }

    double pavg = (mini * mini + maxi * maxi) / 2;
    double t = 2 / (1 + pavg);
    return t;
}
double boltzman(vector<double> &kbt_values, vector<double> &energies, vector)
