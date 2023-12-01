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

	regex PATTERN("(?=([\\d]|one|two|three|four|five|six|seven|eight|nine))");

	map<string, string> translator = {
		{"one", "1"},
		{"two", "2"},
		{"three", "3"},
		{"four", "4"},
		{"five", "5"},
		{"six", "6"},
		{"seven", "7"},
		{"eight", "8"},
		{"nine", "9"}
	};

	string line;
	int sum = 0;
	while (file >> line) {
		sregex_iterator next = sregex_iterator(line.begin(), line.end(), PATTERN);
		sregex_iterator end;
		string res = "";

		while (next != end) {
			smatch match = *next;
			string string_match = match.str(1);
			if (string_match.size() > 1)
				string_match = translator[string_match];

			res += string_match;
			next++;
		}
		int next_num = (res[0]-48)*10 + (res[res.length()-1]-48);
		sum += next_num;
	}

	cout << "Calibration number is: " << sum << endl;

	return 0;
}