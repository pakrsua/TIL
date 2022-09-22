#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	long long X, Y, W, S, ans_1 = 0, ans_2 = 0, ans_3 = 0;
	cin >> X >> Y >> W >> S;
	// 직선으로만
	ans_1 = (X + Y) * W;

	// 대각선으로만
	ans_2 = (((max(X,Y))-((X+Y)%2))*S)+(((X+Y)%2)*W);

	// 대각선 가고 남은거
	ans_3 = (min(X,Y) * S) + ((max(X,Y)-min(X,Y)) * W);

	cout << min(ans_1, min(ans_2, ans_3));
}