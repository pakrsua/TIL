#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int N, temp;
	vector<int>arrA;
	vector<int>arrB;

	cin >> N;

	// A 입력받기
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		arrA.push_back(num);
	}
	// B 입력받기
	for (int i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		arrB.push_back(num);
	}
	// A, B를 오름차순, 내림차순으로 정렬
	for (int i = 0; i < N; i++) {
		for (int j = i+1; j < N; j++) {
			if (arrA[i] > arrA[j]) {
				temp = arrA[i];
				arrA[i] = arrA[j];
				arrA[j] = temp;
			}
			if (arrB[i] < arrB[j]) {
				temp = arrB[i];
				arrB[i] = arrB[j];
				arrB[j] = temp;
			}
		}
	}
	// ans 에 값을 하나씩 더함
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		ans += arrA[i] * arrB[i];
	}
	cout << ans;
}