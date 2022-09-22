#include<iostream>
using namespace std;

int main()
{
	int N, K;
	cin >> N >> K;
	int num = 1;

	for (int i = 0; i < N ;i++)
	{
		if (N % num == 0)
		{
			K--;
		}
		if (K == 0) break;
		num++;
	}
	if (K > 0)
	{
		cout << '0';
	}
	else
	{
		cout << num;
	}
	
}