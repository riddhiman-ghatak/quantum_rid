#include <bits/stdc++.h>
using namespace std;

const double h_bar = 1;
const double m = 1;
const double dx = 0.01;

double V(double x)
{
    if (x <= 4.5)
    {
        return 9 * exp(-pow((x - 4.5) / 0.6, 2));
    }
    else
    {
        return 5 * exp(-pow((x - 4.5) / 0.6, 2)) + 4;
    }
}

vector<complex<double>> solve_schrodinger(double E)
{
    int N = static_cast<int>(10 / dx) + 1;
    vector<complex<double>> psi(N, complex<double>(0, 0));
    double k = sqrt(2 * m * (E - V(0)) / pow(h_bar, 2));
    psi[0] = complex<double>(1, 0);
    psi[1] = exp(complex<double>(0, -k * dx));

    for (int j = 1; j < N - 1; ++j)
    {
        psi[j + 1] = (2 - 2 * m * (E - V(j * dx)) * pow(dx, 2) / pow(h_bar, 2)) * psi[j] - psi[j - 1];
    }

    return psi;
}

double cal_trans_probability(double E)
{
    auto psi = solve_schrodinger(E);
    double maxi = abs(psi[600]);
    double mini = abs(psi[600]);
    for (int j = 601; j < psi.size(); j++)
    {
        maxi = max(maxi, abs(psi[j]));
        mini = min(mini, abs(psi[j]));
    }
    double pavg = (maxi * maxi + mini * mini) / 2;
    return 2 / (1 + pavg);
}

double classical_trans(double E)
{
    if (E > 9)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

double evaluate_sum(double k_BT, const vector<double> &transmission_probabilities, const vector<double> &energies)
{
    double sum_term = 0;
    for (int i = 0; i < energies.size(); ++i)
    {
        sum_term += (0.1 / k_BT) * transmission_probabilities[i] * exp(-energies[i] / k_BT);
    }
    return sum_term;
}

int main()
{
    vector<double> energies;
    for (double E = 1; E < 15; E += 0.1)
    {
        energies.push_back(E);
    }
    // plot wave function psi^2

    vector<complex<double>> psi_9 = solve_schrodinger(9);
    ofstream mag("magnitude.txt");
    double start = 0;
    double end = 10;
    double dx = 0.01;
    int x = 0;
    for (double i = 0; i < 10 + dx; i += dx)
    {
        mag << i << "\t" << abs(psi_9[x]) * abs(psi_9[x]) << endl;
    }

    mag.close();

    vector<double> transmission_probabilities;
    vector<double> classical_probability;
    for (auto E : energies)
    {
        transmission_probabilities.push_back(cal_trans_probability(E));
        classical_probability.push_back(classical_trans(E));
    }

    // Plot Transmission Probability vs Incident Kinetic Energy
    ofstream qout("trans.txt");
    for (int i = 0; i < transmission_probabilities.size(); i++)
    {
        qout << energies[i] << " " << transmission_probabilities[i] << " " << classical_probability[i] << " " << endl;
    }
    // Calculate Boltzmann
    vector<double> k_BT_values;
    for (double k_BT = 0.1; k_BT <= 2.0; k_BT += 0.1)
    {
        k_BT_values.push_back(k_BT);
    }

    vector<double> quantum_sums;
    vector<double> classical_sums;
    for (auto k_BT : k_BT_values)
    {
        quantum_sums.push_back(evaluate_sum(k_BT, transmission_probabilities, energies));
        classical_sums.push_back(evaluate_sum(k_BT, classical_probability, energies));
    }

    ofstream out("boltspart.txt");
    for (int i = 0; i < classical_sums.size(); i++)
    {
        out << k_BT_values[i] << " " << classical_sums[i] << " " << quantum_sums[i] << endl;
    }

    return 0;
}