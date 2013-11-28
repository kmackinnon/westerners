#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void fgetsHelper(char* input){
	if(input[strlen(input)-1]=='\n'){
		input[strlen(input)-1]='\0';
	}
}

void properType(char* input){
	int garbage;
	while(strcmp(input,"user\0")!=0 && strcmp(input,"sysop\0")!=0){
		printf("Please enter a valid type for the user. Either 'user' or 'sysop'\n");
		scanf("%d",&garbage);
		fgets(input,50,stdin);
		fgetsHelper(input);
	}
}

int menuProgram(){
	int i;
	for(i=1;i>0;i++){
		int input;
		printf("----MENU---- \n");
		printf("1. Add \n");
		printf("2. Delete \n");
		printf("3. Edit \n");
		printf("4. Verify \n");
		printf("5. Help \n");
		printf("6. Quit \n");
		printf("Selection:");
		scanf("%d", &input);
		if(input==6){
			break;
		}
		else if(input==1){
			const char* spacing=",";
			int junk;
			printf("Please enter a username to insert. \n");
			/*This will clear the \n out of the buffer*/
			scanf("%d",&junk);
			int gamma;
			char username[50];
			fgets(username,50, stdin);
			/*I have to get rid of the \n in the username*/
			fgetsHelper(username);
			cipherString(username);
			printf("Test: " "%s",username);
			printf("Please enter a password for this username. \n");
			scanf("%d",&junk);
			char password[50];
			fgets(password,50,stdin);
			/*I have to get rid of the \n again*/
			fgetsHelper(password);
			cipherString(password);
			char type[50];
			char temp[50];
			printf("Please enter a type for this username. \n");
			/*This will get the \n out of the buffer*/
			scanf("%d", &junk);
			fgets(temp,50,stdin);
			fgetsHelper(temp);
			properType(temp);
			/*Now either user or sysop has been input, so it can be stored. and encrypted */
			strcpy(type,temp);
			cipherString(type);
			/*Now I can put the whole String together*/
			char input[50];
			strcpy(input,username);
			strcat(input,spacing);
			strcat(input,password);
			strcat(input,spacing);
			strcat(input,type);
			/*Now I can potentially work with the file. First I must consider if it doesn't exist*/
			FILE *f_add=fopen("password.csv","r");
			if(f_add==NULL){
				FILE *f_add2=fopen("password.csv","a");
				fputs(input,f_add2);
				fclose(f_add2);
			}
			else{
				FILE *f_add=fopen("password.csv","ra+");
				//I will need an array to work with.
				char line[50];
				/*This encountered variable will act like a boolean for me*/
				int encountered=0;
				while(fgets(line,50,f_add)){
					/*I have to see if the username already exists in the file*/						
					if(strncmp(line,input,strlen(username)+1)==0){
						printf("This username is already in password.csv. Did not insert.\n");
						encountered=1;								
						break;
					}
				}
				if(encountered==0){
					/*This means the username wasn't encountered in the file*/
					printf("Inserting the username, password and type now. \n");
					fprintf(f_add, "%s\n",input);
				}
			fclose(f_add);
			}
					
		}
		/*Now I can handle the case of deletion*/
		else if(input==2){
			const char* spacing=",";
			int junk;
			printf("Please enter a username for deletion.\n");
			scanf("%d",&junk);
			char username[50];
			fgets(username,50,stdin);
			fgetsHelper(username);
			cipherString(username);
			char input[50];
			strcpy(input,username);
			strcat(input,spacing);
			/*Now I have to check if the password.csv file exists*/
			FILE *f_delete=fopen("password.csv","r");
			if(f_delete==NULL){
				printf("The password.csv file hasn't been created yet. You can only do so using the Add option.");
				close(f_delete);
			}
			else{
				FILE *f_del2=fopen("password.csv","r");
				FILE *f_temp=fopen("temp.csv","w");
				char line[50];
				int foundCondition=0;
				while(fgets(line,50,f_del2)){
					if(strncmp(line,input,strlen(input))==0){
						printf("Username found. Now deleting \n");
						foundCondition=1;
						continue;
					}
				fprintf(f_temp,"%s",line);
				}
				fclose(f_temp);
				if(foundCondition==0){
					printf("Username not found. Returning to main menu. \n");
				}
				else{
					char command[50];
					strcpy(command,"mv temp.csv password.csv");
					system(command);
				}
			fclose(f_del2);
			}	
		}
		else if(input==3){
			const char* spacing=",";
			int junk;
			printf("Please enter an existing username to edit.\n");
			scanf("%d",&junk);
			char olduser[50];
			fgets(olduser,50,stdin);
			fgetsHelper(olduser);
			cipherString(olduser);
			printf("Please enter the password for this existing username.\n");
			scanf("%d",&junk);
			char oldpass[50];
			fgets(oldpass,50,stdin);
			fgetsHelper(oldpass);
			cipherString(oldpass);
			printf("Please enter the type of this existing user.\n");
			scanf("%d",&junk);
			char temp1[50];
			char oldtype[50];
			fgets(temp1,50,stdin);
			fgetsHelper(temp1);
			properType(temp1);
			/*Now the proper type is stored in temp1*/
			strcpy(temp1,oldtype);
			cipherString(oldtype);
			printf("Please enter the new username for this user.\n");
			scanf("%d",&junk);
			char newuser[50];
			fgets(newuser,50,stdin);
			fgetsHelper(newuser);
			cipherString(newuser);
			printf("Please enter the new password for this user.\n");
			scanf("%d",&junk);
			char newpass[50];
			fgets(newpass,50,stdin);
			fgetsHelper(newpass);
			cipherString(newpass);
			printf("Please enter the new type for this user.\n");
			scanf("%d",&junk);
			char newtype[50];
			char temp2[50];
			fgets(temp2,50,stdin);
			fgetsHelper(temp2);
			properType(temp2);
			/*Now the proper type is stored in temp2*/
			strcpy(newtype,temp2);
			cipherString(newtype);
			printf("Test: " "%s", newtype);
			/*Now I can put of these together to be evaluated*/
			char check[50];
			strcpy(check,olduser);
			strcat(check,spacing);
			strcat(check,oldpass);
			strcat(check,spacing);
			/*I need the username and password only as a check later on*/
			char olduseoldpass[50];
			strcpy(olduseoldpass,check);
			strcat(check,oldtype);
			/*Now for the other one*/
			char insertion[50];
			strcpy(insertion,newuser);
			strcat(insertion,spacing);
			strcat(insertion,newpass);
			strcat(insertion,spacing);
			strcat(insertion,newtype);
			/*Finally, I can work with files again, not in place*/
			FILE *f_edit=fopen("password.csv","r");
			if(f_edit==NULL){
				printf("password.csv hasn't been created yet. You must do so through the add option \n");
				fclose(f_edit);
			}
			else{
				FILE *f_temp=fopen("temp.csv","w");
				FILE *f_org=fopen("password.csv","r");
				char line[50];
				/*This will be my boolean expression to see if something was edited*/
				int editcheck=0;
				while(fgets(line,50,f_org)){
					if(strncmp(line,check,strlen(olduseoldpass))==0){
						printf("Old username and password found. Editing now.\n");
						editcheck=1;
						fprintf(f_temp,"%s",insertion);
						continue;
					}
					fprintf(f_temp,"%s",line);
				}
				fclose(f_temp);
				if(editcheck==0){
					printf("Old username and password not found. Returning to main menu. \n");
				}
				else{
					char rewritecommand[50];
					strcpy(rewritecommand,"mv temp.csv password.csv");
					system(rewritecommand);
					printf("Editing successful. Returning to main menu. \n");
				}
			fclose(f_org);
			}
		}
		else if(input==4){
			/*This is the case for verify*/
			const char* spacing=",";
			int rubbish;
			printf("Please enter an existing username to search for. \n");
			scanf("%d",&rubbish);
			char user[50];
			fgets(user,50,stdin);
			fgetsHelper(user);
			cipherString(user);
			printf("Please enter the password for this existing username. \n");
			scanf("%d",&rubbish);
			char pass[50];
			fgets(pass,50,stdin);
			fgetsHelper(pass);
			cipherString(pass);
			char searchable[50];
			strcpy(searchable,user);
			strcat(searchable,spacing);
			strcat(searchable,pass);
			strcat(searchable,spacing);
			/*Now that the username and password have been grouped together, I can start working with the file*/
			FILE *f_verify=fopen("password.csv","r");
			/*I have to check if it exists*/
			if(f_verify==NULL){
				printf("You must create the password.csv file. You can do so through the Add switch. \n");
			}
			else{
				int found=0;
				char line[50];
				while(fgets(line,50,f_verify)){
					if(strncmp(line,searchable,strlen(searchable))==0){
						printf("VALID \n");
						found=1;
						break;
					}
				}
				if(found==0){
					printf("INVLAID \n");
				}
			fclose(f_verify);
			}	
		}
		else if(input==5){
			printf("This is the menu version of the passweb.c program.\n");
			printf("\n");
			printf("Type 1 to add a new username to the password.csv file. \n");
			printf("If a username already exists in the password.csv file, an error message will come on screen.\n");
			printf("If the password.csv file does not exist, this is the option you must choose to create it as well. \n");
			printf("\n");
			printf("Type 2 to delete an existing username and password from the password.csv file. \n");
			printf("You must only know the username of the user that you want to delete.\n");
			printf("\n");
			printf("Type 3 to edit an existing username and password from the password.csv file. \n");
			printf("You must know both the username and the password of a user to edit their \n");
			printf("information. \n");
			printf("\n");
			printf("Type 4 to verify if a username and password exist in the password.csv file. \n");
			printf("You must know both a user's username and password to use this option. \n");
			printf("If found, VALID will be returned. INVALID will be returned otherwise. \n");
			printf("\n");
			printf("Type 5 to get this help message again.\n");
			printf("\n");
			printf("Type 6 to exit the program. \n");
			printf("\n");
			printf("If you type anything else, an error message will be shown on screen.\n");
			printf("\n");
		}			
		else{
		printf("Error: Invalid menu choice. \n");
		printf("Please input 1,2,3,4,5 or 6. \n");
		}
	}
	return 0;
}
