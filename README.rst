|Build Status| |Code Health| |Codacy Badge| |idaplugin PyPI| |server PyPI|

rematch
=======

REmatch, a simple binary diffing utility that just works. 

At least, we hope it will be. Rematch is still a work in progress and is not
fully functional at the moment.  We're currently working on bringing up basic
functionality. Check us out again soon, or watch for updates!

It is intended to be used by reverse engineers by revealing and identifying
previously reverse engineered similar functions and migrate documentation
and annotations to current IDB. It does that by locally collecting data about
functions in your IDB and uploads that information to a web service (which
you're supposed to set up as well). Upon request, the web service can match
your functions against all (or part) of previously uploaded functions and
provide matches.

A secondary goal of this (which is not currently pursued) is to allow
synchronization between multiple reverse engineers working on the same file.

Goal of REmatch
===============

The goal of REmatch is to act as a maintained, extendable, open source tool
for advanced assembly function-level binary comparison and matching. 
Hopefully, this will be a completely open source and free (as in speech) 
community-driven tool.

We've noticed that although there are more than several existing binary
matching tools, there's no one tool that provides all of the following:

#. Open source and community driven.
#. Supports advanced matching algorithms (ML included ™).
#. Fully integrated into IDA.
#. Allows managing multiple projects in a single location.
#. Enables out of the box one vs. many matches.
#. Actively maintained.

Status updates
==============

We'll try to occasionally update here about what's going on in the project
and briefly describe advancements we've had.

Current status (March 1st, 2017)
-----------------------------------

We recently got another big PR in, `Match results dialog
<https://github.com/nirizr/rematch/pull/17>`_, that ended up being more then
just implementing the match results dialog. It shows graphs of remote 
functions being matched, it has a python based scripting to filter the 
match results, it had quite a bit of speedup improvements to the matching
engine as well as fixing some related bugs. 
We also added the concept of "file version" as part of the architecture.
Additionally, we've added more matchers and more annotations ( with more 
coming on the way).
We had some major code quality improvements and improved the plugin and 
server installation process.

Our current goal is the first relase, which requires:

#. Basic documentation being in (partially done).
#. Server deployments using docker and easier installation (in progress).

And will optionally have:

#. Web interface for the server.
#. An achievements / score system. Yay gamification!

Old statuses
------------

Old status paragraphs will be pushed here.

(November 9th, 2016)
++++++++++++++++++++

We recently got a big PR in, `implement match backend
<https://github.com/nirizr/rematch/pull/22>`_, that basically sets up the
foundations for matching functions (as well as some basic matching
functionality). It implements "collectors" (under
`idapython/rematch/collectors`) and "matchers" (under `server/collab/matches`)
which collect features and match functions based on those features
respectively. One of the goals here was to have adding additional matching
strategies and features as easy as possible.

There's no nice way to see the results of such comparisons but they're stored
in the database and the browsable API can be used to view them. Adding a
results dialog is the next big task. We have some basic match configuration
going on for the matching process such as which functions to match and against
what (there's a picture in the PR ticket). 

We also added quite a bit of minor changes (bug fixes, speedup and 
architecture improvements, richer UI).

(August 30th, 2016)
+++++++++++++++++++

Development advances on a daily basis. We have a basic server and an IDA
plugin. We collect a few relatively simple features and working on adding more.
We have a matching stab that we will populate soon. Features are uploaded to
the server. Basic plugin settings, project hierarchy and user authentication.
We have a skeleton for the match results dialog (which supports some basic
python scripting! :D).

.. |Build Status| image:: https://travis-ci.org/nirizr/rematch.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/nirizr/rematch
.. |Code Health| image:: https://landscape.io/github/nirizr/rematch/master/landscape.svg?style=flat
   :alt: Code Health
   :target: https://landscape.io/github/nirizr/rematch/master
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/244945976779490d8f78706a9d4ab46b
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/rematch/rematch?utm_campaign=Badge_Grade
.. |idaplugin PyPI| image:: https://img.shields.io/pypi/v/rematch-idaplugin.svg
   :alt: rematch-idaplugin PyPI
   :target: https://pypi.python.org/pypi/rematch-idaplugin
.. |server PyPI| image:: https://img.shields.io/pypi/v/rematch-server.svg
   :alt: rematch-server PyPI
   :target: https://pypi.python.org/pypi/rematch-server
