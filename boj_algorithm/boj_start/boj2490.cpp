#include<iostream>
using namespace std;

int main()
{
	
	for (int i = 0; i < 3; i++)
	{
		int yut;
		int arr[4];
		char ans;
		int cnt = 0;

		for (int j = 0; j < 4; j++)
		{
			cin >> yut;
			if (yut == 1) cnt++;
		}

		if (cnt == 0) ans = 'D';
		else if (cnt == 1) ans = 'C';
		else if (cnt == 2) ans = 'B';
		else if (cnt == 3) ans = 'A';
		else ans = 'E';

		cout << ans << '\n';
	}
}