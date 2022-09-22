#include<iostream>
using namespace std;
// º° Âï±â - 8

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N-1; i++)
	{
		for (int j = 0; j < i+1; j++)
		{
			cout << '*';
		}
		for (int j = 0; j < N * 2 - ((i+1) * 2);j++)
		{
			cout << ' ';
		}
		for (int j = 0; j < i+1; j++)
		{
			cout << '*';
		}
		cout << '\n';
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N-i; j++)
		{
			cout << '*';
		}
		for (int j = 0; j < ; j++)
		{
			cout << ' ';
		}
		for (int j = 0;j < N-i; j++)
		{
			cout << '*';
		}
		cout << '\n';
	}
}