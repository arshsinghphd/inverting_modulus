## Class Project Proposal 
# Inverting Modulus and Decoding Linear Ciphers

### Group Members (Northeastern Emails)
(Last name lexicographical order)
* Parker McKillop (mckillop.p@northeastern.edu)
* Oksana Pooley (pooley.o@northeastern.edu)
* Arsh Singh (singh.a5@northeastern.edu)

### Category or Type of Project:

* Topic Investigation and 
* Educational Resource

## Project Brief

In very brief, we will implement a function that will implement the Extended Euclid's Algorithm to find the inverse of a modulus function. To go along with this, we will make a flask-based interactive app. The app will call our function and produce all the works for a user provided problem, or when there is a lack of that, randomly generated problems.

We will also make a work along text tutorial that shows how to use our function to solve a rather fun albeit elaborate problem of decoding linear cipher from Fell et al.

### Motivation
In this section, we answer the question why is this a good class project for CS5002.

The main idea of the project is explore how to efficiently find multiplicative inverse of a mod function. Mathematically, to look for a multiplicative inverse of $A \mod B$ is to look for an integer $x$ such that $Ax = 1 \mod B.$ 

We think this is a great class project because it is just beyond what has been taught to us, in other words it is an extension of the class. It is a difficult enough problem that does not solve very easily by hand or even calculators and needs one to implement a function. It is not a purely academic exercise and has uses in cryptography for encryption, decryption, and for sumcheck style integrety check on transmitted messages and  unpackaged computer softwares etc. Time-wise, the project of creating an app with the function as an engine is just-enough dificult that we will be able to do it well in two weeks' time. And most importantly, as a use case for this project we will solve a fun linear cipher puzzle (Exercise 5.7 Page 65 of Fell, Harriet, and Javed A. Aslam. *Discrete Structures*. Cognella academic publishing, 2017).

### Goals
The project will have many three parts, two involve creating python based functions and third is a use case.

#### Function for Mod Inverse
1. Functions for the engine:
   1. Reviewing modulus function. Understanding it enough to find multiplicative inverse using mod tables. Implementing the solution with mod tables.
   2. Implementing a more nuanced algorithm called extended Euclid to find multiplicative inverse.
   3. Writing the above two functions so that these can, if asked, print out all the works.
   4. The functions will also be a module that can be downloaded into the folder and then imported into a python code.
   
#### Flask-Based App/Tutorial
2. Functions for GUI to interact with the user outside of python code in two modes: verbose (show all the works) or not. There will be a function for randomly generated A and B if user does not have a problem in mind.

#### Decoding Linear Ciphers (using our function)
3. A use case of linear cipher decoding using our app.


### Timeline

|Item | Due Date | Person |
| :- | :- | :- |
|Proposal |Due Th, Nov. 20th, end of the day|One of us can email |  
|Draft proposal |Due W, Nov 19th, end of day|Arsh, Oksana, Parker|
|Writing and testing Functions | Nov 20 - 25| Arsh, Oksana, Parker working together on teams shared VS code|
|Writing and testing GUI |Nov 26 - Dec 1 |Arsh, Oksana, Parker working together on teams shared VS code |
|Use case | Dec 2 |Arsh, Oksana, Parker working together on teams shared VScode |
|Use case | Dec 3-5 |Arsh, Oksana, Parker working together on teams shared VScode |
|Project Report | Dec 6-7 |Arsh, Oksana, Parker different parts |
|Project | Dec 8 |One of us can email |

### Expected Outcome

We expect the function to be able to produce well formatted equations to find the multiplicative inverse of $A\mod B$ such as the following, based any positive integers $A$ and $B$  provided to it. We expect it do it in $\log(n)$ time, where $n$ is the bigger number among $A$ and $B$ (usually $B$ if $A\mod B$ is in standard form).

```
First Part: Euclidean Algorithm

Euclidean algorithm gives us the following equations.

2001 = 197 * 10 + 31 	... (1)
197 = 31 * 6 + 11 	... (2)
31 = 11 * 2 + 9 	... (3)
11 = 9 * 1 + 2 	... (4)
9 = 2 * 4 + 1 	... (5)

Second Part: Reversing

Isolating 1 from (5)
1 = 9 * 1 + 2 * -4 	... (6)

Isolating 2 from (4) and putting in (6).
Rearrange to keep as a linear combination of 11 and 9:
1 = 11 * -4 + 9 * 5 	... (7)

Isolating 9 from (3) and putting in (7).
Rearrange to keep as a linear combination of 31 and 11:
1 = 31 * 5 + 11 * -14 	... (8)

Isolating 11 from (2) and putting in (8).
Rearrange to keep as a linear combination of 197 and 31:
1 = 197 * -14 + 31 * 89 	... (9)

Isolating 31 from (1) and putting in (9).
Rearrange to keep as a linear combination of 2001 and 197:
1 = 2001 * 89 + 197 * -904 	... (10)

Because we want a positive multiplicative inverse
replace -904 with -904 + k * 2001, such that -904 + k * 2001 > 0.
In this case, k = 1 and we replace -904 with 1097.
Also find new coefficient of 2001 as 89 - k * 197 = -108, since k = 1

Finally:
1 = 2001 * -108 + 197 * 1097	 ... (11).

Bézout's coefficients are -108 and 1097.

The multiplicative inverse of 197 mod 2001 is:
1097
```
---
### References

Fell, Harriet, and Javed A. Aslam. *Discrete Structures*. Cognella academic publishing, 2017

Grinberg, Miguel. Flask Web Development: Developing Web Applications with Python. 2nd ed., O’Reilly Media, 2018. O’Reilly Online Learning, https://learning.oreilly.com/library/view/flask-web-development/9781491991725/.

Rosen, Kenneth H. *Discrete Mathematics and Its Applications*. 7th ed., McGraw-Hill Education, 2012. 

---
### Project Proposal Guidelines (For Reference, To Be Deleted Before Submission)

The project proposal should contain the following information:

* The name and Northeastern emails of all group members
* The title of the project
* The type of project
* A paragraph or two explaining, at a high level, the motivation and goals of the project
* A high-level framework as to how you will investigate and proceed with the project
* A breakdown of expected distribution of major tasks/topics across group members
* One member of the group must email your group's project proposal to me by the deadline
accompanied by a direct message via Teams to alert me of the submission. All other group
members must be cc’d. Your proposal will be replied to in around 24 to 48 hours, even if
submitted weeks before the deadline. Thus, the earlier a group submits the proposal the earlier you will receive feedback. 

The project proposal is not expected to be perfect, but should show some thought and
effort to make an interesting project, of a scope reasonable for 2 full weeks of serious group effort, and with some initial ideas as to how your group will proceed (such as by what time certain checkpoints will be reached and who is primarily responsible for what portion of the project). Reading these project proposals gives me the opportunity to reach out to you and your group mates sooner rather than later so I may assist you in refining things such as the scope of the project (which may be too small to receive full credit or too large to be completed). 

While I do not have a fixed list of types of project, I provide some examples of project
“types” here:
* Topic Investigation: Collaboratively investigate some concept beyond the base scope
of the course and express your group's understanding of it, potential applications of it,
and how it both builds and expands upon what you learned in the course.
* Educational Resource: Write a resource to introduce and teach a topic from the
course, providing the basic introduction, an intuitive walkthrough with examples,
exercises with clearly stated purposes as to their value for the students, answer keys,
etc.
* Practical: Finding a practical application for some of the more mathematical/theoretical
content of this course, investigating this application, implementing an algorithm based on
this investigation (or several algorithms and doing benchmarking), and reporting on
various performance results, implementation pitfalls for future users to be wary of, etc.
* Original Research: Focus on a singular use case or topic and try to solve a novel
problem within this space. An example would be improving on a known algorithm in
some environment, providing a theoretical framework for understanding some topic,
writing a novel algorithm for a problem and systematically testing its performance, etc.