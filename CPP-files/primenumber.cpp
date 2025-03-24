#include <iostream>
#include <vector>

using namespace std;

int main() {
for (int i = 2; i <= 100; i++) {
// 1 is not a prime number
	bool isPrime = true;
	for (int j = 2; j < i; j++) {
	  if (i % j == 0) {
		  isPrime = false;
	  }	
	}
	if (isPrime) {
	cout << i << " ";
	}

}


}
