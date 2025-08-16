###  I have completed this task.
before going through this task i have learnt some commands for the terminal in ubuntu,and I installed Git through terminal command such as```sudo apt install git```. I will be sharing terminal commands and git commands that i have learnt and used them while solving this task.(I used google to know about the git commands and ```git --help```command from the terminal to find the accurate commands to use)


# Approach
### 1. Find the Facility
I used ```cd``` command to navigate into Terminal-Hunt. I have understood that from the problem statement that we have to find the word **facility**. So for that i got to know that grep command is my weapon to solve this (I got to know after so many searches in google and understandings) . Finally I got it!

And The -r option in grep as it is used for recursive search.
```grep -r "word_to_findout" directory/``` :

This allows you to search for a pattern not only within the specified directory but also in all its subdirectories. Finally I found where the facility is ..


<img width="1610" height="275" alt="Screenshot from 2025-08-16 09-16-28" src="https://github.com/user-attachments/assets/c3ab036a-d170-4f01-98e3-253067269fcf" />


To find the whole message i went to that file by my output from the terminal.


<img width="2036" height="1038" alt="image" src="https://github.com/user-attachments/assets/89f1d6ab-2112-4a20-bb69-6af7a8e1f603" />


### 2. Enter the wormhole
I understood that the wormhole is in saturn and then we have to switch in between the root i.e, G so i went on to saturn by ```cd Saturn ``` command and used the same command to find the  word **wormhole**.


<img width="1732" height="1258" alt="Screenshot from 2025-08-13 22-49-17" src="https://github.com/user-attachments/assets/528ba50f-c6fc-40b0-9dc1-bd3eea2ec5a9" />


I found it but to find the actual message i used the same command for the word "echo".
here's is what i found.


<img width="2108" height="1336" alt="Screenshot from 2025-08-13 22-53-32" src="https://github.com/user-attachments/assets/ed02f645-e1d4-4e92-952b-159f4b49a0b8" />


### 3. Analyze the planets in Gargantuan System
I felt frustrated of this word "Gargantuan". because firstly i wasn't able to understand how i gonna find this. After spending some time on this i found that it was in another branch. then I used some git commnads to navigate into that branch, and i used the grep command to find out the word "habitable" in this GargantuanSystem.

From the various planents in this system ..I found these:


<img width="1996" height="207" alt="Screenshot from 2025-08-16 09-46-41" src="https://github.com/user-attachments/assets/505397c1-5d2d-4ae3-b8e4-05fcd95cf6eb" />


<img width="2026" height="200" alt="Screenshot from 2025-08-16 09-47-37" src="https://github.com/user-attachments/assets/78adf159-4c1c-446f-9e4d-f8b27bc51d24" />


<img width="2045" height="203" alt="Screenshot from 2025-08-16 09-48-32" src="https://github.com/user-attachments/assets/98783120-25f5-44f1-8dbf-bf990d8790e1" />


### 4. Gargantua
Finally by similar way from above sub tasks , I Found my Finall message in The Gargantua Planent in gargantua system 
branch.

here it is the final message:

<img width="2108" height="1336" alt="Screenshot from 2025-08-16 09-49-37" src="https://github.com/user-attachments/assets/cd2b6adb-3bfc-4bb9-912a-c0fa2d199672" />


# Commands Learnt
## Terminal Commands in Ubuntu
```cd <directoryname>```: to change directory

```touch```: to create a file

```grep```: searchs for a particular word with in files

```mkdir```:to make a directory

```sudo```: to make any command run

```ls```: to list out the files or directories

```pwd```: to move to present working directory

```cd ..```: to move to previous 

```ls -a```:to see the hidden files or directories

## Git Commands

```git init```: initializes a directory as a git repository

```git clone <url>```: clones a particular repo to our local system from url

```git add <filename>```: adds a file into staging area (which will be ready to commit)

```git status```: displays which files are added & ready to commit  and which are not added

```git branch```: displays the total branches and in which branch in we are

```git checkout <branchname>```: switches us in between the branches 

```git commit```: used to commit the changes to local repository

```git commit -m "anymessage"```: creates a new commit with the staged changes and includes the provided message as the commit message

```git push```: Pushes the local branches changes to the remote repository
















