#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

namespace std
{

    const double hbar = 1.0;
    const double m = 1.0;

    double V(double x)
    {
        return 0.0;
    }

    vector<double> rk4_step(const vector<double> &psi, const vector<double> &x, double dt, double dx)
    {
        int N = psi.size();
        vector<double> k1(N), k2(N), k3(N), k4(N), new_psi(N);
        double fac = -1j * hbar / (2 * m) / (dx * dx);

        for (int i = 0; i < N; i++)
        {
            int ip1 = (i + 1) % N;
            int im1 = (i - 1 + N) % N;
            double f1 = fac * (psi[ip1] - 2 * psi[i] + psi[im1]) - V(x[i]) * psi[i];
            k1[i] = dt * f1;
        }

        for (int i = 0; i < N; i++)
        {
            int ip1 = (i + 1) % N;
            int im1 = (i - 1 + N) % N;
            double f2 = fac * (psi[ip1] + k1[ip1] / 2 - 2 * (psi[i] + k1[i] / 2) + psi[im1] + k1[im1] / 2) - V(x[i]) * (psi[i] + k1[i] / 2);
            k2[i] = dt * f2;
        }

        for (int i = 0; i < N; i++)
        {
            int ip1 = (i + 1) % N;
            int im1 = (i - 1 + N) % N;
            double f3 = fac * (psi[ip1] + k2[ip1] / 2 - 2 * (psi[i] + k2[i] / 2) + psi[im1] + k2[im1] / 2) - V(x[i]) * (psi[i] + k2[i] / 2);
            k3[i] = dt * f3;
        }

        for (int i = 0; i < N; i++)
        {
            int ip1 = (i + 1) % N;
            int im1 = (i - 1 + N) % N;
            double f4 = fac * (psi[ip1] + k3[ip1] - 2 * (psi[i] + k3[i]) + psi[im1] + k3[im1]) - V(x[i]) * (psi[i] + k3[i]);
            k4[i] = dt * f4;
        }

        for (int i = 0; i < N; i++)
        {
            new_psi[i] = psi[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6;
        }

        return new_psi;
    }

    int main()
    {
        const double x_min = 0.0;
        const double x_max = 10.0;
        const int N = 1000;
        const double dx = (x_max - x_min) / (N - 1);
        vector<double> x(N);
        for (int i = 0; i < N; i++)
        {
            x[i] = x_min + i * dx;
        }

        const double dt = 0.0001;
        const int num_time_steps = 300;
        const vector<int> times = {150, 300};

        const double sigma = 0.1;
        const double k = 20.0;
        const double x0 = 5.0;
        const double alpha = 20.0;
        const double N_const = pow(2 * alpha / M_PI, 0.25);

        vector<double> psi_init(N);
        for (int i = 0; i < N; i++)
        {
            psi_init[i] = N_const * exp(-pow(x[i] - x0, 2) / (2 * sigma * sigma)) * exp(-1j * k * x[i]);
        }

        vector<double> psi = psi_init;
        vector<vector<double>> psi_squared;
        psi_squared.push_back(vector<double>(N));
        for (int i = 0; i < N; i++)
        {
            psi_squared[0][i] = norm(psi_init[i]);
        }

        for (int i = 0; i < num_time_steps; i++)
        {
            psi = rk4_step(psi, x, dt, dx);
            if (find(times.begin(), times.end(), i + 1) != times.end())
            {
                psi_squared.push_back(vector<double>(N));
                for (int j = 0; j < N; j++)
                {
                    psi_squared.back()[j] = norm(psi[j]);
                }
            }
        }

        ofstream file_t0("t0.txt");
        for (int i = 0; i < N; i++)
        {
            file_t0 << x[i] << "\t" << psi_squared[0][i] << endl;
        }
        file_t0.close();

        ofstream file_t150("t150.txt");
        for (int i = 0; i < N; i++)
        {
            file_t150 << x[i] << "\t" << psi_squared[1][i] << endl;
        }
        file_t150.close();

        ofstream file_t300("t300.txt");
        for (int i = 0; i < N; i++)
        {
            file_t300 << x[i] << "\t" << psi_squared[2][i] << endl;
        }
        file_t300.close();

        return 0;
    }

}