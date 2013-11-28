#include <stdlib.h>
#include <stdio.h>
#include <string.h>
const int keyval=5;
/*This helper function will Caesar cipher a String for me*/
void cipherString(char* input){
	/*My key for this assignment will be a shift of 5.*/
	int key=5;
	int k;
	for(k=0;k<strlen(input);k++){
		//This is the first group of ascii values to consider
		if(input[k]<=126&&input[k]>=32){
			int temp=input[k];
			temp=(((temp-32)+key) %95)+32;
			input[k]=temp;
		}
	}
}	
void encrypt(char array[50]){
	/*I will have to divide this into three groups, the ASCII values before ',' after ',' and after DEL.*/
	int i=0;
	while(array[i]!='\0'){
		if(array[i]<44 && array[i]>=32){
			int temp=array[i];
			temp=(((temp-32)+keyval)%13)+32;
			array[i]=temp;
		}	
		else if(array[i]>44 && array[i]<=126){
			int temp=array[i];
			temp=(((temp-44)+keyval) %83) +44;
			array[i]=temp;
		}
		i++;
	}
}
void decrypt(char array[50]){
	int j=0;
	/*Again, three groups will be needed here*/
	while(array[j]!='\0'){
		if(array[j]<44 && array[j]>= 32){
			int temp=array[j];
			temp=(((temp-32)-keyval+13)%13)+32;
			array[j]=temp;
		}
		else if(array[j]>44 && array[j]<=126){
			int temp=array[j];
			temp=(((temp-44)-keyval+83)%83)+44;
			array[j]=temp;
		}
		j++;
	}
}
