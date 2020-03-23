# Auto-E-Books

A simple program that automates downloading e-books, based mainly on [selenium](https://www.selenium.dev/) and [bs4](https://pypi.org/project/beautifulsoup4/).

### Directions for use:
Open the python script and enter the name of the book (academics related, non-fiction or fiction) you want in the 'name' variable, specify the path of the directory you want the download to happen in the 'download_path' variable, run the script and wait a few seconds for the process to complete. 

--------
  ### What this program does:
 - Goes to [Library Genesis](http://libgen.is/)
 - Searches for the name of the book entered by the user.
 - Obtains the list of all the results, extracts all the titles, finds best match for the entered input using [difflib](https://docs.python.org/3/library/difflib.html)
 - If no such book exists, a message expressing the same is printed.
 - Then torrent file for the best match is  then downloaded in a directory which can be changed easily by the user.
 - The default name of the downloaded file doesn't make sense, thus it is renamed automatically to the book's name which was entered by the user.
 - The downloaded torrent file can now be opened by any standard software, like  [bittorrent](https://www.bittorrent.com/).

---
### Future prospects:
- Create a GUI and make this script an executable.
- Automate torrent to PDF conversion.
