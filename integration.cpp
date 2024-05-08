#include <iostream>
#include <cmath>

const double g = 9.8;
const double c = 12.5;
const double m = 68.1;

double integrand(double t)
{
    return 1 - exp(-(c / m) * t);
}

int main()
{
    // 2-point GLQ
    double x2_1 = -0.5773502691896257;
    double x2_2 = 0.5773502691896257;
    double w2_1 = 1.0;
    double w2_2 = 1.0;

    double integral_2pt = 0.0;
    integral_2pt += w2_1 * integrand(50 * (x2_1 + 1));
    integral_2pt += w2_2 * integrand(50 * (x2_2 + 1));
    integral_2pt *= 50 * g * m * c;

    std::cout << "2-point GLQ: " << integral_2pt << std::endl;

    // 3-point GLQ
    double x3_1 = -0.774596669241483;
    double x3_2 = 0.774596669241483;
    double x3_3 = 0.0;
    double w3_1 = 0.555555555555556;
    double w3_2 = 0.555555555555556;
    double w3_3 = 0.888888888888889;

    double integral_3pt = 0.0;
    integral_3pt += w3_1 * integrand(50 * (x3_1 + 1));
    integral_3pt += w3_2 * integrand(50 * (x3_2 + 1));
    integral_3pt += w3_3 * integrand(50 * x3_3);
    integral_3pt *= 50 * g * m * c;

    std::cout << "3-point GLQ: " << integral_3pt << std::endl;

    // Exact value
    double exact_value = 289.4351;
    std::cout << "Exact value: " << exact_value << std::endl;

    return 0;
}