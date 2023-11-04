#include <stdio.h>
#include <ctype.h>


void clean_and_print(char c);



int main() {
	while(! feof(stdin)) {
		char c = fgetc(stdin);
		clean_and_print(c);
	}
}

/*
Input: A character from the unprocessed input
Return: None
Prints a character, if necessary
*/
void clean_and_print(char c) {
	if (islower(c)) {
		/*
  		If the character is a lowercase letter, print it
  		*/
		printf("%c", c);
	} else if (isalpha(c)) {
		/*
 		If the character is an uppercase letter, convert it to lowercase
  		*/
		printf("%c", tolower(c));
	} else if (isdigit(c) || isspace(c)) {
		/*
 		If the character is another "regular character", print it
		*/
		printf("%c", c);
	}
	/*
 	Other characters (like punctuation) are not printed
 	*/
}
