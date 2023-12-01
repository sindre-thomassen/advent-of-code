#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <iterator>
#include <regex>

using namespace std;

int main() {
	ifstream file;
	file.open("../input.txt");

	regex PATTERN("[\\d]");

	string line;
	int sum = 0;
	while (file >> line) {
		sregex_iterator next = sregex_iterator(line.begin(), line.end(), PATTERN);
		sregex_iterator end;
		string res = "";

		while (next != end) {
			smatch match = *next;
			string string_match = match.str();
			
			res += string_match;
			next++;
		}
		int next_num = (res[0]-48)*10 + (res[res.length()-1]-48);
		sum += next_num;
	}

	cout << "Calibration number is: " << sum << endl;

	return 0;
}