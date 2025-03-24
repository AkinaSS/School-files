#include <string>
#include <vector>
#include <iostream>

using namespace std;

struct state {
    string stateName;
    vector<state*> connectedStates;

    state(string name) {
        stateName = name;
    }
};


void printConnections(int index, state* states[]) {
    for (int i = 0; i < states[index]->connectedStates.size(); ++i) {
        cout << states[index]->connectedStates[i]->stateName << endl;
    }

}

int main() {
    //https://stackoverflow.com/questions/650162/why-cant-the-switch-statement-be-applied-to-strings
    //create states:
    vector<string> stateNames = { "Maryland", "New Jersey", "Wisconsin", "Minnesota", "South Dakota", 
        "Missisipi", "Arkansas", "Texas", "Hawaii", "Alabama", "Alaska", "Colorado", "Utah", "Oregon" };
    
    state* states[stateNames.size()];
    for (int i = 0; i < stateNames.size(); ++i) {
        states[i] = new state(stateNames[i]);
        //cout << states[i]->stateName << endl;
    }

    //Maryland 0
    //no connections

    //New Jersey 1
    //no connections
    
    //Wisconsin 2
    states[2]->connectedStates.push_back(states[3]);

    //Minnesota 3
    states[3]->connectedStates.push_back(states[2]);
    states[3]->connectedStates.push_back(states[4]);

    //South Dakota 4
    states[4]->connectedStates.push_back(states[3]);
    
    //Mississippi 5
    states[5]->connectedStates.push_back(states[9]);
    states[5]->connectedStates.push_back(states[6]);
    
    //Arkansas 6
    states[6]->connectedStates.push_back(states[7]);
    states[6]->connectedStates.push_back(states[5]);

    //Texas 7
    states[7]->connectedStates.push_back(states[6]);

    //Hawaii 8
    //no connections
    
    //Alabama 9
    states[9]->connectedStates.push_back(states[5]);
 
    //Alaska 10

    //Colorado 11
    states[11]->connectedStates.push_back(states[12]);
 

    //Utah 12
    states[12]->connectedStates.push_back(states[11]);

    //Oregon 13
    //no connections
    

    printConnections(5, states);

    return 0;
}
