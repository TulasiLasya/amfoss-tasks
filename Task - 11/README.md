By doing this task I learnt how to use terminal for different different situations and I came to know so many different commands to use.

### Here are the list of Topics that I had learnt and used them:
* Connecting a server using ssh key.
* To find out the hidden files from directory.

  * ```ls -a```
* To read some files named with spaces and symbols.
  
   *  ```cat ./"<file symbol>"```
   *  ``` cat ./"<file name>"``` or ```cat spaces\ in\ this\ filename ```
* To find out the file based on the size
   * ``` find . type f -size <size of file>```  if the file size is bytes we use ```c``` at end of files size.
* To find out the file based on username and permission.
   * ```find / -user <username> -group <groupname> -size <filesize> 2>/dev/null.```
   * we use``` 2>/dev/null ``` to remove unwanted lines.
* To use a ```grep``` command to find out a word in a file.
   * ```grep <word> <filename>```
* To find unique lines
   * ``` sort <filename> | uniq -u ```
* To find strings from a file
   * ``` strings -a <filename>```
* To decode ROT13
   * ```cat <filename> | tr 'A-Za-z' 'N-ZA-Mn-za-m'``` 
* To encode binary data into text.
   * ``` cat <filename> | base64 -d```
* To decommpress the file using ```xxp``` , ```gzip``` and ```tar```.
* The ```nc``` command for network communication with another localhost.
  
