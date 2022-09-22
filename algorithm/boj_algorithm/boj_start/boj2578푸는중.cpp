#include<iostream>
using namespace std;
int arr[5][5];
int cnt = 0;
int bingo = 0;

void check()
{
	bingo = 0;
	cnt++;
	//가로 빙고 확인
	for (int i = 0; i < 5; i++)
	{
		if (arr[i][0] == 0 && arr[i][1] == 0 && arr[i][2] == 0 && arr[i][3] == 0 && arr[i][4] == 0)
		{
			bingo++;
		}
	}
	//세로 빙고 확인
	for (int i = 0; i < 5; i++)
	{
		if (arr[0][i] == 0 && arr[1][i] == 0 && arr[2][i] == 0 && arr[3][i] == 0 && arr[4][i] == 0)
		{
			bingo++;
		}
	}
	// 대각선 빙고 확인
	for (int i = 0; i < 5; i++)
	{
		if (arr[i][i] == 0 && arr[i+1][i+1] == 0 && arr[i+2][i+2] == 0 && arr[i+3][i+3] == 0 && arr[i+4][i+4] == 0)
		{
			bingo++;
		}
		else if (arr[i][4 - i] == 0 && arr[i+1][3-i] == 0 && arr[i+2][2-i] == 0 && arr[i+3][1-i] == 0 && arr[i+4][i] == 0)
		{
			bingo++;
		}
	}
}

int main()
{
	// 빙고판
	
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cin >> arr[i][j];
		}
	}
	/*for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cout << arr[i][j] << " ";
		}
		cout << '\n';
	}*/
	
	for (int a = 0; a < 5; a++)
	{
		for (int b = 0; b < 5; b++)
		{
			int num;
			cin >> num;
			cout << "사회자가 부른 수" << num << endl;
			for (int i = 0; i < 5; i++)
			{
				for (int j = 0; j < 5; j++)
				{
					if (arr[i][j] == num)
					{
						arr[i][j] = 0;
						check();
					}
				}
			}
		}
	}
	//cin >> num;
	//cout << "사회자가 부른 수" << num << endl;
}