#include <iostream>

struct student {

    std::string name;
    struct student* next;
};

student* create(std::string studname, struct student* previousStudent) {
    student* newStudent = new student();
    newStudent->name = studname;
    if (previousStudent != 0) {
        previousStudent->next = newStudent;
    }
    newStudent->next = 0;
    return newStudent;
    
}

int main() {
    std::string input;
    student* firstStudent = new student();
    student* previousStudent = firstStudent;

    std::cout << "Enter students name: ";
    std::cin >> input;

    previousStudent->name = input;
    create(input, 0);

    while (int on = 1)
    {
        std::cout << "Do you want to add another student? (y/n): ";
        std::cin >> input;

        if (input == "n") {
            break;
        }
        else if (input == "y")
        {
            std::cout << "Enter students name: ";
            std::cin >> input;

            student* newstu = create(input, previousStudent);
            std::cout << newstu->name << "\n";
            previousStudent = newstu;
        }
        
    }
    
    student* currentStudent = firstStudent;
    while (currentStudent->next != 0)
    {
        std::cout << currentStudent->name << "\n";
        currentStudent = currentStudent->next;
    }
    std::cout << currentStudent->name << "\n";

return 0;
}