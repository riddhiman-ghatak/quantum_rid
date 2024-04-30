#include <iostream>
#include <cmath>
#include <complex>
#include <vector>
#include <fstream>

using namespace std;

const double hbar = 1.0;
const double m = 1.0;
const double dx = 0.01;
const int n = 1000; // Number of points
const double xmin = 0.0;
const double xmax = 10.0;

double V(double x)
{
    if (x >= 4 && x <= 5.0)
    {
        return 9;
    }
    return 0;
}

// Complex function
complex<double> exponent(double k, double x)
{
    return exp(complex<double>(0, -k * x));
}

// Function to calculate wavefunction
vector<complex<double>> func(double E)
{
    vector<complex<double>> psi(n, 0);
    double k = sqrt((2 * E) / hbar);

    psi[0] = exponent(k, xmin);
    psi[1] = exponent(k, xmin + dx);

    // Calculate wavefunction using finite difference method
    for (int j = 1; j < n - 1; ++j)
    {
        double x = xmin + j * dx;
        psi[j + 1] = 2.0 * psi[j] - psi[j - 1] - 2.0 * dx * dx * (E - V(x)) * psi[j];
    }

    return psi;
}

// Function to calculate transmission probability
double transmissionProbability(double E)
{
    vector<complex<double>> psi = func(E);
    double maximum = abs(psi[600]);
    double minimum = abs(psi[600]);

    // Finding maximum and minimum for pavg
    for (int j = 601; j < psi.size(); j++)
    {
        maximum = max(maximum, abs(psi[j]));
        minimum = min(minimum, abs(psi[j]));
    }

    double pavg = (maximum * maximum + minimum * minimum) / 2;
    return 2 / (1 + pavg);
}

int main()
{
    // Output transmission probability to file
    ofstream transmissionFile("transmission_probability.txt");
    for (double E = 1.0; E <= 26.01; E += 0.1)
    {
        double transmission = transmissionProbability(E);
        transmissionFile << E << "      " << transmission << endl;
    }
    transmissionFile.close();

    // Output wavefunction to file
    ofstream wavefunctionFile("wavefunction.txt");
    vector<complex<double>> psi = func(9);
    int i = 0;
    for (double x = 0.0; x <= 10.01; x += 0.01)
    {
        wavefunctionFile << x << "      " << abs(psi[i]) << endl;
        i++;
    }
    wavefunctionFile.close();

    return 0;
}