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

- [ ] Draft steps to parse a CSV file (see [path to
  automation](#path-to-automation))
  - [ ] Create template CSV file based on bank info
  - [ ] Create template CSV file based on utility info
  - [ ] Consolidate where possible, find common values and group
  - [ ] Crosswalk templates to proposed database structure, ID gaps
  - [ ] Create Python function to read data from bank CSV
  - [ ] Create Python function to read data from utility CSV
  - [ ] Create Python function to store data in a dataframe variable
    - Likely to use the Pandas library here
    - Add Pandas dependency to virtual environment
    - Single dataframe object for bank info
    - Single dataframe object for utility info
  - [ ] Research patterns -
    - [ ] Python writing to a file, then having SQL pick up the file to process
      on a schedule (pull pattern)
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
