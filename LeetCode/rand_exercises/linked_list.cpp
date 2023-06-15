#include <vector>
#include <iostream>
#include <memory>

using namespace std;

vector<int> create_arr(int size) {
    vector<int> arr;
    for (int i = 0; i < size; i++) {
        arr.push_back(i);
    }
    return arr;
}

int main(int args, char *kvargs[]) {
    vector<int> arr = create_arr(10);
    for (int index : arr) {
        cout << arr[index] << endl;
    }
    cout << "Done" << endl;
    return 0;
}

