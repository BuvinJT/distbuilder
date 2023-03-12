## Additional Project Goals

In addition to everything which is already fleshed out and functional within it, 
"Distribution Builder" will soon supply a **new development paradigm**...  Using the 
obfuscation and library management features, it will provide the ability for collaborators 
to work on a **Python** project together, **without directly sharing source code**!

We acknowledge this idea may to be deemed "anti-Pythonic" by purists, since the language is
commonly employed for open source purposes, and the Python ecosystem is almost 100%
open source.  Note that the "Distribution Builder" developers are not anti-open source!
In fact, observe that this project is itself open source, and built over the top of other open 
source projects!  We are, however, pro-security, and we advocate for the owners of 
intellectual property. We argue that if it is not universally "wrong" to produce 
close sourced programs, doing so should not be dubbed off limits with Python,
if an organization or individual so choses.   

Once theses features (in development) are completed and smoothed over, each Python developer 
on a project could independently create libraries with a clear text 
*public* interface, but which employ code bases that are obfuscated.  Other developers 
could then implement the functionality of those libraries as they develop their modules.
"Distribution Builder" could next seamlessly bring together everyone's work into a single 
project, where all of the protected code bases work together and even the "seams" between 
those public interfaces become obfuscated. In this scenario, each developer will have this 
capability, and therefore be able to test their own work - on the fly - within the context 
of the larger product.  

Producing software in this manner, allows engineers to work together 
on endeavors where there are gray areas pertaining to intellectual rights and/or the
legalities of such have yet to be solidified.  This mechanism mitigates the risk
of an individual stealing an entire code base, or being "boxed out" of a project for
which they made considerable contributions.  

While this overarching *concept* has long been available with other languages (e.g. with 
C++ dll's and other analogous compiled components), this has not generally been an option 
for Python.  Even in those languages where such is a "ready option", a development scheme 
of this nature is often too cumbersome to employ, or simply not an option developers have
considered. "Distribution Builder" aims to make this a painless and realistic mode of 
operation for Python.

## Important Notes

At the present time, the weakest components in the library are admittedly the obfuscation 
features. There is a bit of a learning curve for utilizing such, and a fair degree of 
effort is likely required to perfect it for your own project right now.  It is recommended 
that you employ these security features only after getting the rest of your build process 
defined.
