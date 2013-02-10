===============================================================
lazy4chan
===============================================================

What it does ?
===============

Fetches all the the files (jpg, jpeg, gif) from a 4chan thread. So if you got a winrar thread, you won't have to save them by hand.

Requirements
-
  - BeautifulSoup ( is available via pip ` sudo pip install BeautifulSoup`)

Running it:
-
  - `git clone https://github.com/DTailor/lazy4chan.git`
  - `sudo pip install -r requirements.txt`
  - Open *main.py* and edit the link variable with the corresponing url.
  - Run in console `python main.py`
  - The files are save in the same directory with the *main.py* file, but in a new folder corresponing to the thread's ID.
 
To-do:
-
  - Make it as a shell tool with [docopt](https://github.com/docopt/docopt) package 
