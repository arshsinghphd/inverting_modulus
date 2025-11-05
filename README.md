# Inverting Modulus and Decoding Linear Ciphers
## CS5002 Fall2025 Class Project
### Parker McKallop, Oksana Pooley, and Arsh Singh

We create a function that estimates the multiplicative inverse of a modulus.

It is accompanied by a video description of how we created the function.

To make it more instructive, we also use our function to solve a rather fun, but elaborate problem from Fell, Harriet, and Javed A. Aslam. *Discrete Structures*. Cognella academic publishing, 2017. The solution is provided as a PDF work along using out flask-based application.

**Technical Aspects**
* Finding multiplicative inverse of a modulus function is neither intutive nor is it straightforward. It requires understanding of many important underlying concepts.
* Our function not only finds the multiplicative inverse, but if asked, also prints out all the 'works' - the various algebraic steps taken to reach it.
* There is a detailed docstring description that shows how to use the functions. 
* There also are several use cases in the docstrings.
* All functions are originally written from a decription of the Reverse Eulid Algorithm provided in Rosen, Kenneth H. *Discrete Mathematics and Its Applications*. 7th ed., McGraw-Hill Education, 2012. 
* There are innovations for using data structures that are not in the pseudocode. This functions ensures everything is done in O[log n] time and is able to reproduce all the work as numbered equations. 
* Looking at the clean well written output, one may think an LLM is somehow involved, but it's not.
* This function is created in python. 
* We used Flask to make its HTML based GUI.
* We referred to Grinberg, Miguel. Flask Web Development: Developing Web Applications with Python. 2nd ed., O’Reilly Media, 2018. O’Reilly Online Learning, https://learning.oreilly.com/library/view/flask-web-development/9781491991725/.