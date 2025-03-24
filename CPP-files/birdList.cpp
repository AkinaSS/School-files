#include <iostream>
#include <string>
using namespace std;

struct bird {
	string name;
	bird* beak;
};

int main() {
	bird* head = 0;
	bird* tail = 0;
	string userInput;

	bird chicken;
	chicken.name = "chicken";
	chicken.beak = 0;

	head = &chicken;
	tail = &chicken;

	while (true) {
		cout << "Insert a new bird:";
		cin >> userInput;
		if (userInput == "q") {
			break;
		}
		bird* newBird = new bird();
		newBird->name = userInput;
		newBird->beak = 0;
		head->beak = newBird;
		tail = newBird;
	}

	//cout << chicken.name;
	 
	return 0;
}
