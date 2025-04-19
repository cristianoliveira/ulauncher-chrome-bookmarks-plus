# ulauncher-chrome-bookmarks-plus

An advanced fork of [ulauncher-browser-bookmarks](https://github.com/pascalbe-dev/ulauncher-browser-bookmarks) see: [this fork features](#this-fork-features)

> [ulauncher](https://ulauncher.io/) Extension to quickly open chrome bookmarks.

## Demo

https://github.com/pascalbe-dev/ulauncher-browser-bookmarks/assets/26909176/c39d9610-fe8d-4e1f-89e5-cff483bd1992

## Features

### This fork features

- Filter by folders
- Configurable sort method
  - Sort by Most Visited
  - Sort by Last Visited
  - No Sort
- Bookmark indexing for performance

### Upstream

- search and open browser bookmarks
  - search by single text (must be contained in the bookmark title)
  - search by multiple texts split by space (all must be contained in the bookmark title)
- supports multiple browser profiles
- supports multiple browsers 
  - Google Chrome
  - Chromium
  - Brave
  - Vivaldi
  - other chromium based browsers by specifying the browser config path in the extension settings

## Requirements

- [ulauncher 5](https://ulauncher.io/)
- Python > 3

## Installation

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

`https://github.com/pascalbe-dev/ulauncher-browser-bookmarks.git`

## Contribution

Please refer to [the contribution guidelines](./CONTRIBUTING.md)

## Local development

### Requirements

- `less` package installed
- `inotify-tools` package installed

### Getting started

1. Clone the repo `git clone https://github.com/pascalbe-dev/ulauncher-browser-bookmarks.git`
2. Cd into the folder `cd ulauncher-browser-bookmarks`

3. Install the requirements `pip install -r requirements.txt` or simply 
```bash
pip install -r requirements.txt --user
## or
make setup
```

4. Running
```bash
make start
```

5. Once you are done
```bash
make stop
```

### Tests

To run the unit tests
```bash
make test
```

### Quality insurance

- install the ruff via `pip install -r requirements.txt`
- run formatting via `ruff format`
- run linting via `ruff check`

### Local testing

1. Watch and deploy your extension locally for simple developing and testing in parallel `./watch-and-deploy.sh` (this will restart ulauncher without extensions and deploy this extension at the beginning and each time a file in this directory changes)
2. Check the extension log `less /tmp/ulauncher-extension.log +F`
3. Check ulauncher dev log `less /tmp/ulauncher.log +F`
