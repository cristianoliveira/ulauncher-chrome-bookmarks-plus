from typing import Any, List, Dict
import json

type BookmarkEntry = Dict[str, Any]


class BookmarkQuerier:
    bookmarks: BookmarkEntry

    def __init__(
        self, bookmarks: List[BookmarkEntry] = [], filter_by_folders: bool = False
    ) -> None:
        """
        Initializes the BookmarkQuerier class.
        Parameters:
            filter_by_folders (bool): Whether to filter by folders
        """
        self.filter_by_folders = filter_by_folders
        self.max_matches_len = 10

        # length of bookmarks json
        self.bookmarks_hash = []
        self.indexed_bookmarks = {}
        self.index_list(bookmarks)

    def index_list(self, bookmarks: List[BookmarkEntry]) -> None:
        """
        Indexes a list of bookmarks into "{name} {url}": {bookmark_entry} format.
        Recursively indexes all bookmarks and folders.

        :param bookmarks: The bookmarks to index.
        """
        for b in bookmarks:
            hashed = hash(json.dumps(b))
            if hashed not in self.bookmarks_hash:
                self.bookmarks_hash.append(hash(json.dumps(b)))
                self.index(b)

    def index(
        self, bookmarks: BookmarkEntry, parent: str = ""
    ) -> Dict[str, BookmarkEntry]:
        """
        Indexes the bookmarks into "{name} {url}": {bookmark_entry} format.
        Recursively indexes all bookmarks and folders.

        :param bookmarks: The bookmarks to index.
        :return: A dictionary of indexed bookmarks.
        """
        if not bookmarks.get("type"):
            return {}

        if bookmarks.get("type") == "folder":
            for child_bookmark_entry in bookmarks["children"]:
                parent_tree = f"{parent} {bookmarks.get('name')}".strip()
                if parent_tree == "root":
                    parent_tree = ""
                self.index(child_bookmark_entry, parent_tree)
        else:
            bookmark_title = bookmarks["name"]
            bookmark_url = bookmarks.get("url", "")

            # Create search text that includes parent folder name, bookmark name and URL
            search_text = f"{bookmark_title} {bookmark_url}"
            if self.filter_by_folders and parent:
                search_text = f"{parent} {search_text}"

            self.indexed_bookmarks[search_text] = bookmarks

        return self.indexed_bookmarks

    def search(
        self,
        bookmark_entry: Dict[str, Any],
        query: str,
        matches: List[Dict[str, Any]],
        parent_name: str = "",
    ) -> None:
        """
        Searches for a query in the indexed bookmarks.
        Matches if query terms are found in either name, URL, or parent folder name.

        Parameters:
            bookmark_entry (Dict[str, Any]): The bookmark entry to search
            query (str): The query
            matches (List[Dict[str, Any]]): The list to append matches to
            parent_name (str, optional): The name of the parent folder
        """
        hashed = hash(json.dumps(bookmark_entry))
        if hashed not in self.bookmarks_hash:
            self.index(bookmark_entry, parent_name)

        for search_text, bookmark in self.indexed_bookmarks.items():
            # Check if the search text contains all query terms
            if self.contains_all_substrings(search_text, query.split()):
                matches.append(bookmark)

    def contains_all_substrings(self, text: str, substrings: List[str]) -> bool:
        """
        Check if all substrings are in the text

        Parameters:
            text (str): The text to match against
            substrings (List[str]): The substrings to check

        Returns:
            bool: True if all substrings are in the text, False otherwise
        """
        for substring in substrings:
            if substring.lower() not in text.lower():
                return False
        return True
