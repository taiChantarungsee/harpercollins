NOTE: In order to get the app to work, a copy of the spreadsheet file has to be in the app directory.

Install requirements using:

`python pip install -r requirements.txt`

Then go into the `main.py` file and replace twitter credentials. Simply `python main.py` that file to start the script.

The last function schedules several twitter uploads based on the dates obtained in the spreadsheet so you'll need to tweak
those dates, if you want to see it working. The UKPyth twitter account already has both bulk and scheduled posts uploaded.
Exit from the scheduler function by hitting CTRL-Z. 

Also beware of double posting - Twitter won't allow this. 

Overall this project could do with a lot more refactoring. Due to time contraints I ended up with two many nested for loops,
the wait time can definietely be reduced, using a variety of tools such as map(), filter() and enumerate() from itertools.
