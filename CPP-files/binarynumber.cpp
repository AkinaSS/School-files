#include <iostream>

using namespace std;

bool isBinary(int number) {
	while (number > 0) {
		int digit = number % 10;
		if ((digit != 0) && (digit != 1)) {
			return false;
		}

		number = number / 10;
	}

	return true;
}

int main() {
	int num;
	cin >> num;

	if (isBinary(num)) {
		cout << num << " is a binary number" << endl;
	}
	else {
		cout << num << " is not a binary number" << endl;
	}
}
