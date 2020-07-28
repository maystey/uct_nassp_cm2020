# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
the version number, `a.b.c`, follows the following scheme:

- `a`. The edition (0 for the initial, incomplete edition), this will generally change on a yearly basis.
- `b`. New chapter(s) added or drastically changed, the number increase is the number of chapters added/changed
- `c`. New sections, corrections, etc. The number change is consecutive, not reflecting the number of changes.

## [1.0.0] - 2020-07-28

### Added

- Chapter: Numerical Solutions to ODEs, Numerical Root Finding, Numerical Integration, Astropy

## [0.11.0] - 2020-05-06

### Added

- Chapter: File I/O, Matplotlib, Regression and Scipy
- Section: Numpy:Array Conditional Statements and numpy.where()

### Changed

- Edited CHAPTERS, removing the completed sections for the sake of readability

## [0.8.0] - 2020-03-09

### Added

- Chapters: Functions, Benchmarking, NumPy

### Changed

- Edited Basics:String Formatting, If Statements:If Statements
- Update Gems

## [0.5.1] - 2020-02-11

### Added

- Sections Loops: Breaking Out of Loops and Else Statements and Loops

### Changed

- Edited Intro, Basics:Variables,Functions,Strings (fixed broken tables) and Data Structures: Tuples, Lists

### Bugs Fixed

- Table in Basics:Variables now renders properly (now embedded html)


## [0.5.0] - 2020-02-11

### Added

- Chapter: Introduction (along with bib items)

### Changed

- Updated Jupyter-Book to 0.6.4 .
- Edit Home page.
- Edited Basics: Variables and Comments.
- Replaced the Jupyter Book logo with the UCT logo. Still need to replace the favicon.
- Moved the Data Structures chapter to before the If Statements chapter.
- Chapter contents are no longer expanded in the sidebar. The sidebar was already too long and that was only a quarter of the contents.

### Bugs

- Search function no longer works.
- Page titles are using toc even though they are set to none in config. Need to decide if the pages should loose their in document titles to accommodate.

## [0.4.1] - 2020-01-22
### Added

- If Statements section from the chapter of the same name to toc (and therefore the site). This was unintentionally omitted in the previous build.

### Changed

- Added link to the book site to README.
- Split the Basics/Strings section into Basics/Strings and Basics/String Formatting. Noticed there is a bug in String Formatting caused by a Jekyll Liquid syntax error.

### Fixed

- The site now works. Updated the _config.yaml file with the appropriate website base and url; and rebuilt the html.
- Replaced the `_` with `-` in each directory and notebook filename as this was incompatible with the html build process.

## [0.4.0] - 2020-01-20
### Added

- Chapter: Basics.
- Chapter: If Statements.
- Chapter: Data Structures.
- Chapter: Loops
- This CHANGELOG file.
- The README file.
- The CHAPTERS file for keeping track of the progress of the chapters (including milestones).