Zero Comments
=============

This project consists of some individual code examples, which attempt to test
the principle of "Zero Comments" &ndash; the idea that you should do everything
you possibly can to make your code more readable, *without* adding any comments.
In particular, you should make your source code as readable as it can be
by choosing each identifier in the code, i.e. class, method or variable
name, to be as accurate as possible as a description of whatever it actually represents.

Code Notes
----------

In practice, everyone comes to code with a different level of knowledge about whatever the
code is for.

In an attempt to see how far one can go *without* putting any comments in the code, I
have put *all* additional code documentation and explanation in the accompanying README.
(The only exception is that where it is appropriate to give credit for other related code in the code
itself, I have done so.)

So, if you think that you already know everything about the subject of the code, you can go
straight into the code and see how easily you can understand it.

But if you get stuck, read the accompanying README file, and then go back into the code.

Branch Notes
------------

In the **commented** branch in this Git repository, I have added a minimum level of comments
to the code examples, which would normally expected as a coding standard for code intended
to be shared with or maintained by other developers (or even to be maintained by oneself at a
later date.

This does not discount the benefits of writing code which is documented using only careful
choice of names in the code, complemented by separate README files containing necessary background
information and code notes.

The approach of writing code without comments *and* satisying the requirement to comment classes and methods
can be combined by applying a three-step process:

1. Write self-descriptive code with zero comments.
2. Add README's with background information and code notes.
3. Then, add class and method comments to the code.

To merge this process with the normal process of making changes to code, the results of steps 2 and 3
can be maintained in separate source code branches.

In the current repository, branch *master* holds the result of step 2, and *commented* holds the result
of step 3.
