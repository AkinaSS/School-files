/*Write a minimum of three classes - at least one higher level class, 
and two others that inherited from that higher level class. (Such as how cat and dog inherit from animal.)

These classes should have at least public methods and private data, 
though you can optionally have private methods as well. (The public methods can be used to access the private data.)*/
#include <iostream>
#include <string>
using namespace std;

class Vehicles {
protected:
    string make;
    string model;
public:
    Vehicles(string make, string model) {
        this->make = make;
        this->model = model;
    }
};

class Cars : public Vehicles {
    private:
        string engine;
    public:
        Cars(string make, string model, string engine) : Vehicles(make, model) {
            this->engine = engine;
        }

        void display() {
            cout << "Make: " << make << endl;
            cout << "Model: " << model << endl;
            cout << "Engine: " << engine << endl;
        }
};

class Bikes : public Vehicles {
    private:
        string brakes;
    public:
        Bikes(string make, string model, string brakes) : Vehicles(make, model) {
            this->brakes = brakes;
        }

        void display() {
            cout << "Make: " << make << endl;
            cout << "Model: " << model << endl;
            cout << "Brakes: " << brakes << endl;
        }
};

class Boats : public Vehicles {
    private:
        string motor;
    public:
        //c++ declaration version of this->motor = motor;
        Boats(string make, string model, string motor) : Vehicles(make, model), motor(motor) {}

        void display() {
            cout << "Make: " << make << endl;
            cout << "Model: " << model << endl;
            cout << "Motor: " << motor << endl;
        }
};

class Planes : public Vehicles {
    private:
        string engine;
    public:
        //c++ declaration version of this->engine = engine;
        Planes(string make, string model, string engine) : Vehicles(make, model), engine(engine) {}

        void display() {
            cout << "Make: " << make << endl;
            cout << "Model: " << model << endl;
            cout << "Engine: " << engine << endl;
        }
};

int main() {
    Cars car = Cars("Lamborghini", "Aventador", "V12");
    Bikes bike = Bikes("Kawasaki", "Ninja", "Brembo");
    Boats boat = Boats("Yamaha", "WaveRunner", "Jet");
    Planes plane = Planes("Boeing", "747", "Jet");

    car.display();
    bike.display();
    boat.display();
    plane.display();

    return 0;
}