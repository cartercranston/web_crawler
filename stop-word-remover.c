#include <stdio.h>
#include <string.h>
#include <ctype.h>


#define MAX_WORD_LENGTH 40
#define MAX_LINE_LENGTH 2000
#define MAX_WORDS_PER_LINE 200
#define NUM_STOP_WORDS 9

char stop_words[NUM_STOP_WORDS][6] = {"the", "a", "an", "of", "for", "to", "and", "but", "yet"};

void print_line_without_stop_words(char line[]);

short int is_stop_word(char word[]);

void print_words_in_line(char words[][MAX_WORD_LENGTH], int num_words);

void trim_whitespace(char* word);

int main () {
	/*
  	Iterate over standard input. When there are no lines left in the file, fgets will return "downloading" and the program will end.
	*/
	char line[MAX_LINE_LENGTH];
	fgets(line, MAX_LINE_LENGTH, stdin);
	while(line != NULL) {
		print_line_without_stop_words(line);
		/*
 		Get the next line of input from stdin. If there is none, break out of the loop.
 		*/
		if(fgets(line, MAX_LINE_LENGTH, stdin) == NULL) break;
	}
}

/* Input: a line of text in a char array
 * Returns: none
 * Removes stop words from the line, then prints it to stdout
*/
void print_line_without_stop_words(char line[]) {
	char words[MAX_WORDS_PER_LINE][MAX_WORD_LENGTH];
	int i = 0;

	char *token = strtok(line, " ");

	/*
 	Add each word that isn't a stop word to the words array.
 	*/
	while (token != NULL && i < MAX_WORDS_PER_LINE) {
		if (!(is_stop_word(token))) {
			strncpy(words[i], token, MAX_WORD_LENGTH);
			i++;
		}
		
		/*
 		Store the next word in token
 		*/
		token = strtok(NULL, " ");
	}

	/*
 	Print the words array
 	*/
	print_words_in_line(words, i);
}

/* Input: A pointer to a char array
 * Returns: 1 if the array matches a stop word, 0 if it doesn't.
 */
short int is_stop_word(char *token) {
	/*
	Compare the word to each stop word
	*/
	for (int i = 0; i < NUM_STOP_WORDS; i ++) {
		if (strcmp(token, stop_words[i]) == 0) {
			/*
			If any stop words match, the token is a stop word
			*/
			return 1;
		}
	}
	/*
	The token is not a stop word
	*/
	return 0;	
}

/* Input: An array of strings, and the number of strings in the array
 * Returns: none
 * Prints each word to stdout. 
 */
void print_words_in_line(char words[][MAX_WORD_LENGTH], int num_words) {
	for (int i = 0; i < num_words - 1; i++) {
		printf("%s ", words[i]);
	}
	/* 
 	Last word should be printed without added whitespace
  	*/	
	printf("%s", words[num_words - 1]);
}
