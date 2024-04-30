#include <bits/stdc++.h>
using namespace std;

const double k = 1;
const double gam = 0.5;
const double Q = 1.06;
const double Omeg = 2 / 3;

double h = 0.02 * 2 * M_PI;

double f(double y, double z, double l)
{
    return -k * sin(y) - gam * z + Q * sin(l * Omeg);
}

vector<vector<double>> Rk4(double y, double z, double l)
{
    vector<vector<double>> res(250, vector<double>(3, 0));

    for (int i = 1; i <= 250; i++)
    {
        double s1_y = h * z;
        double s1_z = h * f(y, z, l);

        double s2_y = h * (z + 0.5 * s1_z);
        double s2_z = h * f(y + s1_y * 0.5 * h, z + 0.5 * h * s1_z, l + 0.5 * h);

        double s3_y = h * (z + 0.5 * s2_z);
        double s3_z = h * f(y + s2_y * 0.5 * h, z + 0.5 * h * s2_z, l + 0.5 * h);

        double s4_y = h * (z + s3_z);
        double s4_z = h * f(y + h * s3_y, z + h * s3_z, l + h);

        y += (s1_y + 2 * s2_y + 2 * s3_y + s4_y) / 6;
        z += (s1_z + 2 * s2_z + 2 * s3_z + s4_z) / 6;

        l += h;
        res[i - 1][0] = y;
        res[i - 1][1] = z;
        res[i - 1][2] = l;
    }
    return res;
}

int main()
{
    ofstream myfile("data.dat");

    double y = 1, z = 0, l = 0;
    vector<vector<double>> ans = Rk4(y, z, l);
    for (auto x : ans)
    {
        myfile << x[2] << "\t" << x[0] << "\t" << x[1] << endl;
    }
    myfile.close();
}