rename_series
===========

	rename_series is a python application that renames series, subtitles
	and puts the subtitles to the chapters.
	
	Basically, this application search in one (or more directories) for 
	series and subtitles in various languages. 
		* I have series in spanish and english. 
	
	First renames the chapters to a nice format:
		<show name> <season>x<episode> [<episode title>] [(VO)].<extension> 
		
		* The only series taken as spanish are the downloaded from 
			spanishtracker (newpct). You can configure this.
	
	Then renames the subtitles.
	
	Then puts the subtitles to the corresponding chapters, putting the same name
	of the subtitle to the video file.
	
AUTHOR

    Rubén Hortas
    Contact: rubenhortas at gmail.com
    Website: http://www.rubenhortas.blogspot.com.es

LICENSE

    CC BY-NC-SA 3.0
    http://creativecommons.org/licenses/by-nc-sa/3.0/

USAGE

	$ python3 <script>

	or (if you hace python3 as your default version):

	$ ./<script>

	RENAME SERIES

		usage: rename_series.py [-h] [-t] [-d] [-D USER_DIR]

		Renames some series.

		Optional arguments:
  		-h, --help            			show this help message and exit
  		-t, --test            			run a single test showing the expected output
  		-d, --debug           			show debug info
  		-D USER_DIR, --dir USER_DIR	use only the specified directory/path
	
	SEARCH FOR DUPLICATED EPISODES
		
		usage: search_for_duplicated_episodes.py [-h] [-t] [-d] path

		Look for repeated chapters

		positional arguments:
  		path         path where the files are being sought

		optional arguments:
  		-h, --help   show this help message and exit
  		-t, --test   run a single test showing the expected output
  		-d, --debug  show debug info

	SEARCH FOR DUPLICATED IN FILES

		usage: search_for_duplicated_in_files.py [-h] [-from FROM_FILE] [-in IN_FILE]
   		                                      [-t] [-d]

		Look for repeated strings in file[s]

		optional arguments:
  		-h, --help       show this help message and exit
  		-from FROM_FILE  from file
  		-in IN_FILE      in file
  		-t, --test       runs a single test showing the expected output
  		-d, --debug      show debug info

CONTACT

    If you have problems, questions, ideas or suggestions, you can
    contribute with this little project in the github repository:

    https://github.com/rubenhortas/rename_series

WEB SITE

    Visit the rename_series github site for the lastest news and downloads:

    https://github.com/rubenhortas/rename_series
