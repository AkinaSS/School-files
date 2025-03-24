#include <iostream>
#include <string>
using namespace std; 

/*
If you don't already have it, write code that will build a linked list from instances 
of the struct generated from user input. (By appending new members to end of list.)

Then: make methods that will insert instances at any point on the list, and delete 
from any point of the list, without breaking the structure of the list or losing track
of any allocated memory.
*/

struct Animal
{
    string name;
    Animal* point;
};

void insert(string x, string y, Animal* head){
    Animal* middle = head;

    Animal* newAnimal = new Animal;
    newAnimal->name = x;

    while(y != middle->name){
        if(middle->point == nullptr){
            break;
        }
        middle = middle->point;
    }

    if(y == middle->name) {
        newAnimal->point = middle->point;
        middle->point = newAnimal;
    }
    
}

void pop(string animalName,Animal* head){
    Animal* middle = head;
    Animal* prior = head;

    if(middle->name == animalName){
        head = middle->point;
        delete middle;
    }
    else {
        middle = middle->point;

    while(animalName != middle->name){
        if(middle->point == nullptr){
            break;
        }

        middle = middle->point;
        prior = middle->point;
        
        }
        prior->point = middle->point;
        delete middle;
    
    }
}


int main(){
 
Animal* first = nullptr;
Animal* last = nullptr;
string userInput;
string userInput2;
Animal* place;

cout << "Enter a Animal (or q to quit): " << endl;
cin >> userInput;
 
Animal* animal = new Animal;
animal->name = userInput;
first = animal;
last = animal;

// Animal* anotherOne = new Animal;
// anotherOne->name = userInput;
// last->point = anotherOne;
// last = anotherOne;
// cout << "Enter a fruit: " << endl;
// cin >> userInput;

while( ( userInput != "q") && ( userInput !="Q") ) 
{

    cout << "Do you want to add another animal or delete an animal? (a/d): " << endl;
    cin >> userInput;
    if(userInput == "d" || userInput == "D"){
        cout << "What animal do you want to delete?: "<<endl;
        cin >> userInput;
        if(userInput == "q" || userInput == "Q"){
            break;
        }
        pop(userInput, first);
    }
    else if(userInput == "a" || userInput == "A"){
        cout << "What animal would you like to insert: " << endl;
        cin >> userInput;
        cout << "Where would you like to insert: " << endl;
        cin >> userInput2;
        insert(userInput, userInput2, first);
    }

}

place = first;
while(place->point != nullptr)
{
    cout << place->name<<endl;
    place = place->point;
}
    cout << place->name;
    return 0; 
}



