/*Write up the skeletons of 2-4 classes (two large, four small...) including both attribute and methods. 
These should include their types, but does not need to include the actual code. 
These can be for your final project. 
If you aren't ready for that, you can rework some of your final project for last quarter in this structure.*/

#include <iostream>
#include <string>
using namespace std;

// Class 1: Cars
class cars
{
private:
    string engine;
public:
    string model;
    string make;
    int year;

    cars(string model, string make, int year);
    void reveal_engine(int year) {
        if (year < 2000) {
            engine = "V6";
        } else {
            engine = "V8";
        }
        cout << "The engine is a " << engine << endl;
    }
};

class cars2 {
    public:
    string model;
    string make;
    int year;
};

class bikes
{
public:
    string model;
    string make;
    int year;

    bikes(string model, string make, int year);
};

cars::cars(string model, string make, int year)
{
    this->model = model;
    this->make = make;
    this->year = year;
}

bikes::bikes(string model, string make, int year)
{
    this->model = model;
    this->make = make;
    this->year = year;
}

int main() {
    cars car1 = cars("Civic", "Honda", 1999);
    cars car2 = cars("Camry", "Toyota", 2005);
    bikes bike1 = bikes("Ninja", "Kawasaki", 2010);
    bikes bike2 = bikes("R1", "Yamaha", 2015);

    cars2 newCar;
    newCar.model = "Accord";
    newCar.make = "Honda";
    newCar.year = 2010;
    cout << newCar.model << " " << newCar.make << " " << newCar.year << " " << endl;

    car1.reveal_engine(1999);
    car2.reveal_engine(2005);

    cout << car1.model << " " << car1.make << " " << car1.year << " " << endl;
    cout << car2.model << " " << car2.make << " " << car2.year << " " << endl;
    cout << bike1.model << " " << bike1.make << " " << bike1.year << " " << endl;
    cout << bike2.model << " " << bike2.make << " " << bike2.year << " " << endl;

    return 0;
}