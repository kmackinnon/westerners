
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(){
	char string[200];
	char c;
	int a=0;
	int n=atoi(getenv("CONTENT_LENGTH"));
	while((c=getchar())!=EOF &&a<n){
		if(a<200){
			if(c!='+'){
				string[a]=c;
			}
			else{
				string[a]=' ';
			}
			a++;
		}
	}
	string[a]='\0';
	char command[100];
	char username[50];
	char password[50];
	const char* spacing=" ";
	a=0;
	n=strlen(string);
	int i;
	int j=0;
	int k=0;
	int print=0;
	//I have managed to parse for the username that is entered.
	for(i=0;i<n;i++){
		if(string[i]=='='){
			j=i+1;
			while(string[j]!='&'){
				j++;
			}
			k=i+1;
			break;
		}
	}
	strncpy(username,&string[k],j-k);
	username[j-k]='\0';
	//Now I will parse for the password that is entered.
	int numequal=0;
	for(i=0;i<n;i++){
		if(string[i]=='='){
			numequal=numequal+1;
			if(numequal>1){
				j=i+1;
				while(string[j]!='\0'){
					j++;
				}
				k=i+1;
				break;
			}
		}
	}
	strncpy(password,&string[k],j-k);
	password[j-k]='\0';	
	//Now I have both the username and the password. I will work with this.
	//This will compile the passweb.c program in case it hasn't been compiled already.
	system("gcc -o passweb passweb.c");
	//Now to work
	strcpy(command,"./passweb -verify");
	strcat(command,spacing);
	strcat(command,username);
	strcat(command,spacing);
	strcat(command,password);
	strcat(command, " >garbage.txt");
	/*I will pass the total command into the system now*/
	system(command);
	FILE *f_check=fopen("garbage.txt","r");
	char line[50];
	fgets(line,50,f_check);
		/*If EXIT_SUCCESS is found, then you know it's in the password.csv file, so you're done*/
		if(strcmp(line,"EXIT_SUCCESS")==0){
			print=1;
		}
	fclose(f_check);
	
	/* Removing the temporary text file that collected the garbage from Q1. */
	system("rm garbage.txt");

	if(print==1){
		printf("%s%c%c\n",
		"Content-Type: text/html",13,10);
		printf("<body background = \"background.jpg\" link=\"red\">");
		printf("<font color=\"white\"><center><h1>Login Successful!</h1></center></font>");
		printf("<center><font color=\"white\">Congratulations! You logged in successfully!</br></font></center>");
		printf("<center><h1><a href=\"http://cs.mcgill.ca/~kmacki1/ass5/welcome.html\">Welcome Page</a></br></h1></center>");
		printf("<center><h1><a href=\"http://cs.mcgill.ca/~kmacki1/ass5/room.html\">Room Page</a></br></h1></center>");
	}
	else{
	printf("%s%c%c\n",
		"Content-Type: text/html",13,10);
		printf("<body background = \"background.jpg\" link=\"red\" text=\"white\">");
		printf("<center><h1> Login Unsuccessful!</h1></br>");
		printf("</br>");
		printf("<center>Username or Password not found.<center></br>");
		printf("<center>Would you like to go ");
		printf("<a href=\"http://www.cs.mcgill.ca/~jcheve/ass5/login.html\">back</a>");
		printf(" and try again?</center>");
	}
        return 0;
}
