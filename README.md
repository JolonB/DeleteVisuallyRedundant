Delete Visually Redundant
=========================

A Python script that deletes redundant visually-similar images.

For a list of visually similar images it finds, it first deletes all but the largest by file-size.
If still multile files remain, it deletes all but the oldest by modified-on.

How to use
----------

These are the accepted options:

| Option | Description
| ------ | ------------
| -r     | The script creates a 'dups.txt' file as an intermediate while processing. This file holds the list of visually-similar filenames. Giving _-r_ prevents deleting this intermediate file after processing.
| -d     | Dry run. Prints out the names of the files which would be deleted. Doesn't actually delete them.
| -h     | Prints help message


Dependencies
------------

* [`findimagedupes`](https://github.com/jhnc/findimagedupes) - May be available in a package manager

**or**

* `py3findimagedupes` - Available through `git submodule init; git submodule update`
  * This depends on `pgmagick`. Instructions are available in the `py3findimagedupes` README.

Gotchas
-------

* Supports jpg, png and gif files
  - The script can be trivially modified to support even more file types.

Tags
----

duplicate; image; remove; detect; find;
