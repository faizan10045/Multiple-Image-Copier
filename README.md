# Multiple-Image-Copier
Copy multiple images from many source folders to a different destination folders using last few characters of filename. 

Programming Language :- Python

Applications :- Use this code to copy images/files/folders to a destination programmtically instead of manual selection. Weeding/trip/any miscellaneous files.

Back Story:- My family had shortlisted a couple of 100 marraige photos (JPG & ARW) from two different folders contianing 4000+ images in total. After shortlisting best images we had to move them into a new folder to have the final selected images. 

Method_1 :- Normally people would select the images manually and Ctrl+C and Ctrl+V the images in new folder that could take an hour or two.

Method_2 :- As an enigneer, I saw this as an oppurtunity to write a program code to move files and so did I.

Method_2 Solution:-
I used Python. 

1. Import necessary libraries, 
2. Take few variables based on your filename i.e common to all images. For instance it could be like 'DSLR101.jpg, DSLR102.jpg, .... , 'DSLR999.jpg' so here 'DSLR' is common prefix and '.jpg' is common suffix
3. Store your selected filenames inside a list/array/string. In my case I had a string seperated by commas as input from my Family 
4. Split the string into a list/array 
5. Iterate through total count of list/array
6. Add prefix + list[i] + suffix then append it to a new_list
7. Iterate through new_list and use imported functions to copy from source to destination

Note :- please suggest code changes I know this code is not at all optimized, I wrote it in an hour with little help of internet. Time_complexity= O(n^4) and Space_complexity= O(n^2) maybe. 

![image](https://github.com/user-attachments/assets/b6c331c0-a774-40ac-8e7c-d7a67c6ace83)

