# plutus-private

Personal finance application

## Purpose

The purpose of this repository is to build out my personal finance application.
I'll be adding info to this README as time goes on, initial versions of this doc
are going to be pretty sparse.

## Milestones

Capturing major and minor milestones here, minor milestones will be first, with
major milestones following after. I'll be using GitHub's version control to show
progress over time, which means that as I check things off the list of
milestones, they'll disappear from the minor and major sections and move to the
archive section, but you can go back through the history of this doc to see when
each milestone/task was completed.

### Milestone Archive

See [Milestone Archive](/milestone-archive.md) for completed activities.

### Minor Milestones

---

- [ ] Create template CSV file based on utility info - **paused**
- [ ] Consolidate where possible, find common values and group - **paused**
- [ ] Crosswalk templates to proposed database structure, ID gaps - **paused**
- [ ] Create Python function to read data from utility CSV - **paused**
- [X] Update `plutus-intake` to parse bank info as a pipe-delimited CSV file
- [ ] Create regex to add pipes to bank CSV for processing
  - [ ] Open file
  - [ ] Store data from file into variable
  - [ ] Parse data using regex
  - [ ] Output data to file
- [ ] Automate regex script run (add to `plutus-intake`?)
  - Maybe hardcoding this isn't the best idea? Could hardcode then refactor
    later after MVP is working
- [ ] Research patterns -
  - [ ] Python writing to a file, then having SQL pick up the file to process on
      a schedule (pull pattern)
  - [ ] Python writing directly to a temp table in the Dev environment, SQL
      processes data on a schedule (push pattern)
  - [ ] SQL calling python script to read data directly into the DB
- [ ] Research testing
- [ ] Research GitHub pipelines
- [ ] Research badges (Black, linting, passing tests)
- [ ] Pause Python development
- [ ] Start database development
  - [ ] Create MVP database and data structure to house data coming from Python
    MVP app

### Major Milestones

---

- [ ] Use Python + CSV files to parse financial and utility info
- [ ] Create a database to house all financial information
  - [ ] Look into different database languages: sqlite3, T-SQL, etc.
- [ ] Build a frontend or use a tool to visualize the data
  - [ ] SSRS, Power BI, Tableau, R, Python, JavaScript (D3.js, Chart.js,
    Victory.js)
  - [ ] Map out the process and build automation to support operations
- [ ] Document the app
  - [ ] Coding decisions
  - [ ] Loading new data into the database
  - [ ] General usage
  - [ ] Troubleshooting

### Path to Automation

---

- [ ] Use Python to read CSV files and place data into a database
- [ ] Create generic scripts to read different types of CSV files
  - [ ] Financial institution data
  - [ ] Utility data
- [ ] Use Python to identify when a file is dropped into a folder, read it,
  parse it, load it into the database
- [ ] Use Python to scrape information from sites (utility and financial
  institutions)
- [ ] Use Python to log in to sites (need to research a lot in security before
  getting to this point)
- [ ] Automate the entire process

## Links

Section for links (research, etc.)

1. [Goals Repository](https://github.com/K-Mertyris/2022-goals)
