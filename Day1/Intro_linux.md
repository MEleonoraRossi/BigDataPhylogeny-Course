# Intro to Linux/bash 

*by Maria Eleonora Rossi*

During the course we will use the command line for our exercises. The command line is a text-based interface used widely in bioinformatics to interact with computers.
A bit of familiarity with the command line will help you greatly in our practical; however, here is a little refresher on the commands that are going to help you navigate folders, read files, and launch analyses.

Connect to the cluster as explained in the instruction by opening the Terminal on your machine. You'll likely see something like this
```sh
(base) eleonora@mac ~ % 
```
The `%` is called the prompt; on other machines (e.g. Windows) can also look like this `>`.

## Running commands

Once opened the terminal we are ready to run commands. The command is the first you type, normally can be followed by flags or settings introduced by the symbol `-`, that change the default behaviour of the command.

For example:
```sh
(base) eleonora@mac ~ % ls -l 
total 2536
drwxr-xr-x   4 eleonora  staff      128 26 May  2025 Aggresso
drwx------   2 eleonora  staff       64  8 Jul  2024 Apps
```
The first line after the prompt is the command we are executing. In this case `ls` is listing all files and directories in the current working directory. The flag `-l` forces the `ls` command to print the long version of the output with extended information about the directory's content.

We can also specify to list a specific directory to inspect by adding the name of what we want to inspect after the `-l`
```sh
(base) eleonora@mac ~ %  ls -l Conferences/CGUE_eukaryotics 
total 0
drwxr-xr-x  10 eleonora  staff    320 12 Sep  2024 Expenses claim
-rw-rw----@  1 eleonora  staff  57498 20 Aug  2024 Request-for-approval-to-Travel-Oct-2023_CGUE.docx
```

Whenever we want to know how a command works we can type `man` followed by the command. 
```sh
(base) eleonora@mac ~ %  man ls 
```
Another way is to type `-h` or `--help` after the command or program we want to execute.


## Navigating and working in the filesystem

The nested hierarchy of folders and files on your computer is called the filesystem. When we use the computer, we are used to click on the folder or the file we want to open. On the terminal, we cannot do that with a click, but we need to navigate and access the folder (we normally refer to them as directories) we want to open with specific commands. 

All directories are nested within a previous directory, and you can also have multiple directories in the same location, as you would have, for example, different folders in your Finder app. 

To know where we are in the filesystem of our computer or HPC, we can type in the directory `pwd`, short for print working directory.

```sh
ubuntu@ip-172-31-15-77:~$ pwd
/home/ubuntu
```
`/home/ubuntu` is the pathway, and `ubuntu` is the directory I am in. Each directory is separated by `/` symbol.

Let's say we want to create a new directory, normally we would do right click -> new. Here we use the command `mkdir` (make directory).

```sh
(base) eleonora@mac Desktop % mkdir Linux_tutorial
```
To check if we have created the directory, we type `ls` (list), which allows us to see all the files and directories present in the directory we're in.

```sh
(base) eleonora@mac Desktop % ls
Linux_tutorial
```
Now we want to go into the directory we just created. We can use `cd` (change directory) and the name of the directory

```sh
(base) eleonora@mac Desktop % cd Linux_tutorial 
(base) eleonora@mac Linux_tutorial % 

```
Type again `pwd` and check the pathway you're in. Is it similar to the previous pwd?

If we want to exit the directory we are in, we need to 'move back' in the folder. The wildcard to do is `..`, the full command is `cd ..`. This command always moves you one directory back. If you want to move 2 directories back, you just need to type `cd ../../`. Remember to delimit each directory with the `/`. 

Type `cd ..`
What is the path now?

Let's create another directory in `Linux_tutorial` and call it `data`. What would you type?
Enter the directory and check the absolute path.

Ok now we have the basics to navigate the filesystem. Let's see how to work with files.

## Working with files

If we want to know which files are present in the directory we would normally type`ls` or `ll`. If you do it know, in the new directory you have created most likely you will not see anything, sicne it's empty. 
Let's create some files
```sh

touch empty_file
```
Most times, we need to visualise the files. To do so, there are different commands we can use. `less` is very useful; it loads the file you want to visualise, and you can "scroll" the file by hitting the space bar or actually scrolling with the mouse. The advantage of `less` is that it loads in the memory temporarily only the section of the file you are looking at, meaning that it's handy to look at very large files. 
Type `less empty_file`. It will load and you would be able to look inside. The file is now empty so you cannot really see anything. Press `q` on your keyboard to exit the `less` command.

Two other useful commands are `head` and `tail` 
As the names might suggest, `head` shows you the first part of the file. With the flag `-n`, you can specify how many lines you want to see of the file. 
E.g. if you type `head -n 30 <file-name>` you will visualise the first 30 lines of that file.

A similar concept can be applied to `tail`, where it allows you to check the last part of the file. 


## Editing files

The are several text editors you can use to edit a file or a script. One of the easiest to use is `nano`. You can start edit the file by just typing the command and the name of the file you want to edit, or if you want to write a new file just type nano followd by the name you want to give to your file.

```
nano empty_file
```
Once opened, you can move around with the cursor, write, paste, copy, etc, etc. Once done, you can ext `nano` with `ctrl + x`. If the file has been modified, `nano` will ask if you want to save it, and you say yes by typing `y`. The program will then quit, and you will find the file in the directory. 
Try to write your name, save it and exit nano. 
Type `less empty_file` again, can you see your name?


## Wildcards and Pattern Search

Very often in bioinformatics, we need to run the same command hundreds of times on hundred of files. Wildcards are special characters used to match filenames or text patterns in Unix.

Common wildcards:

- `*` → matches any number of characters
- `?` → matches a single character
- `[]` → matches one character from a set
Here are some example of how you can use wildcards. You do not need to run them now.

Let's create some empty files:
```sh 
touch carol.txt blah.txt example.png firstfile.txt number2file 
```

Now we can use the wildcard * to list only the files that begin with the letter b:
```sh

ubuntu@ip-172-31-15-77:~/Linux_tutorial$ ls b*
blah.txt

```
What if we wanted to list all the files that end with .txt?

```sh
username@bash:~/wildcards_test$ ls *.txt  
carol.txt  blah.txt  firstfile.txt 
```
We can use the * wildcard to move files for example
```sh
username@bash:~/wildcards_test$  mkdir images
username@bash:~/wildcards_test$  mv *png images/
username@bash:~/wildcards_test$  ls images/ 
example.png

```
The wildcard `?` represent a single character
For example, it can be used to list all files whose second letter is a:

```sh
username@bash:~/wildcards_test$ ls ?a*
carol.txt
```
In Unix there are many wildcards that can be used to manipulate data, if you want to dig deeper [here](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm) you have a nice summary of all of them.

### Grep command
Another great command that we can use is `grep`. 
The command grep is used to search for patterns inside files, iterating over each line of it. 
It is extremely useful if we want to check for a specific line or character in our files.
E.g. 
```sh
grep "Best-fit model" <name-file>
```
Here we are looking for the line "Best fit model" in a specific file, we could do the same action for multiple file including the * wildcard, for example if we have 30 log files from IQTree that all end with the same `.log` extention we coud run:

```sh
grep "Best-fit model" *log
```
Another useful characteristic of grep is counting. 
Let's say we have a fasta file and we want to count how many sequences we have we can do:

```sh
grep -c ">" file.fasta
```

# Piping and Redirection

Unix allows commands to work together using pipes and redirection.

## Redirection

`>` sends output to a file:

```bash
ls > files.txt
```

`>>` appends output instead of overwriting:

```bash
echo "new line" >> notes.txt
```

`<` uses a file as input:

```bash
sort < names.txt
```

## Pipes

The pipe symbol `|` sends the output of one command into another command.

Count how many files are in the directory:

```bash
ls | wc -l
```
If we want to know all the commands we have run up until now we can use `history`, but let's say we want to search for a specific command.
We could use history piped with grep like this:
```sh
history | grep touch
```

What does it show?

## For Loops

the first practicals of the tutorial we will often use a for loop. This help us running the same command for all the files we need. 
A for loop has normally this structure: for i in *.file ; do <command $i> ; done
- for i in *file = for every item called *file (it can be the common extension, in our case it can be all fasta files, so *.fa, *.fas, *fasta) call it `i` 
- `do command $i` = run the command for all the file we have called `i`, we call back the variable i with a `$` sign
- `done` = end of the loop 

Keep in mind that foor loops can be very useful, however they execute the command for each file one at the time, meaning that they not run in parallel. If you need a quicker solution a job array will be more useful.

## Useful resources
These are just some very basic commands and instructions on how to use the command line. Please come back to this tutorial if you need help while running the phylogenomics practical.

For a more in-depth read, a very good starting book for your first steps in bioinformatics is *Practical Computing for Biologists by Haddoc and Dunn*. You can find more info [here](https://practicalcomputing.org/index.html). 

Finally, here is the [cheat sheet](https://linuxstans.com/bash-cheat-sheet/) for some basic bash commands.
 
Good luck and have fun!