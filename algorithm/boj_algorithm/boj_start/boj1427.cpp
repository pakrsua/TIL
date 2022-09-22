#include<iostream>
#include<string>
using namespace std;

int main()
{
	string num;
	int n;
	cin >> n;
	num = to_string(n);
	// cout << num;

	for (int i = 0; i < num.length();i++)
	{	
		int temp;
		for (int j = i+1; j < num.length();j++)
		{
			if (num[i] < num[j])
			{
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}
	for (int i = 0; i < num.length(); i++)
	{
		cout << num[i];
	}
}