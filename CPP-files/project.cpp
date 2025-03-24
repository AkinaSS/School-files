// liveshare for the group
// https://prod.liveshare.vsengsaas.visualstudio.com/join?

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <cctype>

using namespace std;

 
class Field {
    public:
        string name;
        string location;
        string type;
        bool lights;
    
        Field(string n, string loc, string t, bool l) : name(n), location(loc), type(t), lights(l) {}
    };
    
    class City {
    public:
        string name;
        vector<Field> fields;
    
        City(string n, vector<Field> f) : name(n), fields(f) {}
    
      
    };
    
    vector<City> cities = {
        City("Olympia", {
            Field("Olympia High School", "Olympia", "Turf", true),
            Field("The Evergreen State College", "Olympia", "Grass", false),
            Field("Capital High School", "Olympia", "Turf", true),
            Field("Yauger Park", "Olympia", "Grass", false),
            Field("Jefferson Middle School", "Olympia", "Grass", true),
            Field("Marshall Middle School", "Olympia", "Grass", false),
            Field("Washington Middle School", "Olympia", "Grass", true)
        }),
        City("Lacey", {
            Field("The Regional Athletic Complex", "Lacey", "Turf", true),
            Field("RiverRidge HighSchool", "Lacey", "Grass", false),
            Field("Rainier Vista Park", "Lacey", "Grass", true),
            Field("William A. Bush Park", "Lacey", "Grass", false),
            Field("Komachin Middle School", "Lacey", "Grass", true),
            Field("North Thurston Highschool", "Lacey", "Turf", false),
            Field("Chinook Middle School", "Lacey", "Grass", true)
        }),
        City("Tumwater", {
            Field("Tumwater High School", "Tumwater", "Turf", true),
            Field("Tumwater Middle School", "Tumwater", "Grass", false), 
            Field("Capital Soccer Complex", "Tumwater", "Grass", true),
            Field("Pioneer Park", "Tumwater", "Grass", false),
            Field("Black Hills High School", "Tumwater", "Turf", true)
        })
    };
/*struct for all the colleges to point to*/


void ask_field_preference(int cityIndex);

// Function to check the user input
void check_user_input(char UserInput) {
    UserInput = (char)tolower(UserInput);

    int cityIndex = -1;
    switch(UserInput) {
        case 'o':
            cityIndex = 0;
            break;
        case 'l':
            cityIndex = 1;
            break;
        case 't':
            cityIndex = 2;
            break;
        default:
            cout << "Invalid input" << endl;
            return;
    }

    ask_field_preference(cityIndex);
}


// fucntion for preference of field 
void ask_field_preference(int cityIndex) {
    string field_preference;
    cout << "Do you prefer grass or turf fields? Type 'g' or 't' respectively" << endl;
    cin >> field_preference;
    char prefChar = tolower(field_preference.at(0));

    string lights_preference;
    cout << "Do you prefer fields with lights? Type 'y' or 'n' respectively" << endl;
    cin >> lights_preference;
    char lightsChar = tolower(lights_preference.at(0));

    cout << "You selected " << (prefChar == 'g' ? "grass" : "turf") << " fields with " << (lightsChar == 'y' ? "lights" : "no lights") << endl;
    for (const auto& field : cities[cityIndex].fields) {
        if ((prefChar == 'g' && field.type == "Grass") || (prefChar == 't' && field.type == "Turf")) {
            if ((lightsChar == 'y' && field.lights) || (lightsChar == 'n' && !field.lights)) {
                cout << "Name: " << field.name << ", Location: " << field.location 
                        << ", Type: " << field.type << ", Lights: " << (field.lights ? "Yes" : "No") << endl;
            }
        }
    }
    
}
//     

string wordChecker (string UserInput) { //cant we use && instead of ||?
    char userChar = UserInput.at(0);
    if (userChar == 'o' || userChar == 't' || userChar == 'l' || userChar == 'O' || userChar == 'T' || userChar == 'L'){
        return UserInput;
    }
    while (userChar != 'o' && userChar != 't' && userChar != 'l' && userChar != 'O' && userChar != 'T' && userChar != 'L'){
        cout << "Invalid input" << endl;
        cout << "Select between Olympia, Tumwater, Lacey" << endl << endl;
        cin >> UserInput;
        userChar = UserInput.at(0);
        if (userChar == 'o' || userChar == 't' || userChar == 'l' || userChar == 'O' || userChar == 'T' || userChar == 'L'){
            break;
        }
    }
    cout << "You selected: " << UserInput << endl;
    return UserInput;
}

void autoCorrect(string UserInput){
    vector<string> correctInputUpper = {"Olympia", "Tumwater", "Lacey"};
    vector<string> correctInputLower = {"olympia", "tumwater", "lacey"};
    char conditions = (char)tolower(UserInput.at(0));
    char userChar = UserInput.at(0);
    // cout << userChar << endl;    char check
    if (conditions == 'o') {
        if (UserInput.compare(correctInputUpper[0]) != 0 && UserInput.compare(correctInputLower[0]) != 0){
            switch (userChar)
            {
            case 'O':
                cout << "Autocorrect " << UserInput << " to " << correctInputUpper[0] << endl;
                break;
            default:
                cout << "Autocorrect " << UserInput << " to " << correctInputLower[0] << endl;
                break;
            }
        }
    }
    else if (conditions == 't') {
        if (UserInput.compare(correctInputUpper[1]) != 0 && UserInput.compare(correctInputLower[1]) != 0){
            switch (userChar)
            {
            case 'T':
                cout << "Autocorrect " << UserInput << " to " << correctInputUpper[1] << endl;
                break;
            default:
                cout << "Autocorrect " << UserInput << " to " << correctInputLower[1] << endl;
                break;
            }
        }
    }
    else if (conditions == 'l') {
        if (UserInput.compare(correctInputUpper[2]) != 0 && UserInput.compare(correctInputLower[2]) != 0){
            switch (userChar)
            {
            case 'L':
                cout << "Autocorrect " << UserInput << " to " << correctInputUpper[2] << endl;
                break;
            default:
                cout << "Autocorrect " << UserInput << " to " << correctInputLower[2] << endl;
                break;
            }
        }
    }
}
    
/*this is our main function*/
int main() {

    

    string userInput;
    vector<string> cities = {"Olympia", "Tumwater", "Lacey"};

    while (true) {
        cout << "Pick a city to find soccer fields (q to quit)" << endl;
        for (int i = 0; i < cities.size(); i++) {
            cout << i+1 << ". " << cities[i] << endl;
        }
        cin >> userInput;
        if (userInput == "Q" || userInput == "q") {
            cout << "Goodbye!" << endl;
            break; 
        }
        cout << "You selected: " << userInput << endl;
        string finalInput = wordChecker(userInput);
        autoCorrect(finalInput);
        check_user_input(finalInput.at(0));
        

        cout << "Would you like to search again? (n or q to stop, enter any other letter to continue)" << endl;
        cin >> userInput;
        if (userInput == "N" || userInput == "n" || userInput == "Q" || userInput == "q") {
            cout << "Goodbye!" << endl;
            break;
        }
    }

    return 0;
}