SHOWS MANAGER
===========

    Shows manager is a little framework that allows you easy and/or manage your downloaded tv shows.
    You can:
        - rename your shows to a nice format <SHOW NAME> <SEASON>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION>
        - rename your subtitles to a nice format <SHOW NAME> <SEASON>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION>
        - search for duplicated episodes in an organized disk
        - search for duplicated names into one or two files
        - automatically move files to one or more disks
        
     Requires python >= 3.0

USAGE

rename_shows.py

	This application searches in one or more paths for tv shows and subtitles in various languages. 
    Renames the tv shows to a nice format <SHOW NAME> <SEASON>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION>
    Renames the subtitles to a nice format <SHOW NAME> <SEASON>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION>
    
    usage: rename_shows.py [-h] [-t] [paths [paths ...]]

    Renames some series.

    positional arguments:
    paths       paths to rename files

    optional arguments:
      -h, --help  show this help message and exit
      -t, --test  run a single test showing the expected output


search_for_duplicated_episodes.py

	This application searches for duplicated episodes in an organized disk.
	The disk organization must be in <SHOW NAME>/<SEASON NAME>/<EPISODES> format.
	
	usage: search_for_duplicated_episodes.py [-h] [-t] [-d] dest_path

    Look for repeated chapters
    
    positional arguments:
      dest_path    dest_path where the files are being sought
    
    optional arguments:
      -h, --help   show this help message and exit
      -t, --test   run a single test showing the expected output
      -d, --debug  show debug info

	
search_for_duplicated_in_files.py

    This application searches for duplicated names into one or two files.
    The files could be tv shows and/or movies lists.
    
    usage: search_for_duplicated_in_files.py [-h] [-from file] -in file [-t]

    Look for repeated strings in file[s]
    
    optional arguments:
      -h, --help  show this help message and exit
      -from file  from file
      -in file    in file
      -t, --test  runs a single test showing the expected output

move_shows.py

    This application automatically move files to one or more disks.
    Includes two types of disks:
    
        - Buffer disk: A disk that contains a bunch of unorganized tv shows and/or movies and/or subtitles. 
            Tv shows and subtitles will end in <SHOW NAME> <SEASON>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION>
            format.
            
         - Final disk: A disk that contains organized tv shows.
            Disk structure must be <SHOW NAME>/<SEASON NAME>/<EPISODES>
            Tv shows and subtitles will end in <SEASON NAME>x<EPISODE> [ - <EPISODE TITLE>] [OV].<EXTENSION> format
            inside within their respective path.
            
    usage: move_shows.py [-h] [-to path] [-t]
    
    Move some shows.
    
    optional arguments:
      -h, --help            show this help message and exit
      -to path, --to_path path
                            path to move the files
      -t, --test            Runs a single test showing the output.

AUTHOR

    Rubén Hortas
    Contact: rubenhortas at gmail.com
    Website: http://www.rubenhortas.blogspot.com.es

LICENSE

    CC BY-NC-SA 3.0
    http://creativecommons.org/licenses/by-nc-sa/3.0/

CONTACT

    If you have problems, questions, ideas or suggestions, you can
    contribute with this little project in the github repository:

    https://github.com/rubenhortas/shows_manager

WEB SITE

    Visit the rename_series github site for the latest news and downloads:

    https://github.com/rubenhortas/shows_manager

