# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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