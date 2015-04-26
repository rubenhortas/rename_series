rename_series
===========

	rename_series is a python application that renames series, subtitles
	and puts the subtitles to the chapters.
	
	Basically, this application search in one (or more directories) for 
	series and subtitles in various languages. 
		* I have series in spanish and english. 
	
	First renames the chapters to a nice format:
		<show name> <season>x<episode> [<episode title>][ (VO)].<extension> 
		
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

	$ python3 rename_series
	
	or (if you have python3 as your default version):
	
	$ ./rename_series

CONTACT

    If you have problems, questions, ideas or suggestions, you can
    contribute with this little project in the github repository:

    https://github.com/rubenhortas/rename_series

WEB SITE

    Visit the rename_series github site for the lastest news and downloads:

    https://github.com/rubenhortas/rename_series
