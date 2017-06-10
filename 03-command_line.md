# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

Assume bash shell.
```pwd`` prints the working directory
```mkdir``` creates a directory
```rmdir or rm -rf``` removes a directory, the latter if not empty and forces it.
```touch myfile.txt``` will create an empty file named touch if not present already, otherwise it will update the timestamp.
```rm file``` will remove a file
```mv oldname newname``` will rename a file named oldname to newname.
```ls -a``` will list files that were hidden may starting their name with a dot.
```cp ~/onedir/foo ~/anotherdir/`` will copy the file named foo from the directory named onedir underneath the home directory to one named anotherdir underneath the home directory.
```ps -elf f``` will list the processes in a nice tree format.
```find / -name 'yo*'``` will find a file whose name starts with yo.

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > The ls command lists files, while the arguments adjust which files and how they are shown.  The -a shows the dot files which are normally not shown.  The -l, for long, displays more information such as the mode, owner, group, links and date.  Adding the -h argument, for human readable, additionally shows the sizes with a unit that decreases the number of digits, like 4k instead of 4096 and so forth.  They -lah arguments combines to show all files, including dot files, in long format and with human readable sizes.  The -t will sort the files in time order, with the most recently modified near the top. The -G will omit the group in the long listing and the -p will put an extra forward slash, '/', on directories.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > The `ls -alhrt` command will list all files in long format with human readblae time and do a reverse sort. The `ls -i` will show the inode number and `ls -1` will only list one item per line.

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Breaks up a long list of arguments into groups of one or more to be run at a time. For example ```find /tmp -name 'core.*' -type f -print0 | xargs -P10 --null /bin/rm -f``` will delete core files using 10 threads.



