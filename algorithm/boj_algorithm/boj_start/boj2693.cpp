#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int T;
	cin >> T;

	//num�� �Է¹޾Ƽ� �迭�� �ֱ�
	for (int tc = 0; tc < T; tc++)
	{	
		vector<int>arr;
		for (int i = 0; i < 10; i++)
		{
			int num;
			cin >> num;
			arr.push_back(num);
		}
		//�������� ����
		//�ӽ÷� ���ڸ� ���� ����
		int temp;
		for (int i = 0; i < 10; i++)
		{
			for (int j = i + 1; j < 10; j++)
			{
				if (arr[i] < arr[j])
				{
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}

		}
		//count�� 0���� �����ϱ� ������ 3���� ū ���� �ε����� 2
		cout << arr[2] << '\n';
	}

}
