#include<iostream>
using namespace std;

int main()
{
	int a, b, c, d;
	cin >> a >> b;
	c = a % b;
	d = a * b;
	while (c > 0)
	{
		a = b;
		b = c;
		c = a % b;
	}
	cout << b << '\n' << d / b;
}