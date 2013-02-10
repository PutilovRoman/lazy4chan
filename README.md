===============================================================
lazy4chan
===============================================================

What it does ?
===============

Fetches all the the files (jpg, jpeg, gif) from a 4chan thread. So if you got a winrar thread, you won't have to save them by hand.

Requirements
-
  - BeautifulSoup ( is available via pip ` sudo pip install BeautifulSoup`)
  - docopt (is available via pip `sudo pip install docopt`)

Running it:
-
  - `git clone https://github.com/DTailor/lazy4chan.git`
  - `sudo pip install -r requirements.txt`
  - Run in console `python main.py LINK_URL` or `python main.py LINK_URL FILDER_NAME`
  - The files are saved in the same directory with the *main.py* file, but in a new folder corresponing to the thread's ID or the name specified by the user.
 
To-do:
-
  - Make it available to call this tool from anywhere
