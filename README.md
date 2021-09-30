# Homepage for Behavioral Data Science at UTS

## Dependency
Please make sure you have installed the `hugo` ([v0.60.1](https://github.com/gohugoio/hugo/releases/tag/v0.60.1)) for testing your changes. After cloning the project and making sure you are on the `source` branch, run `bash view.sh` within the project and then you'll be able to view your changes lively at: `localhost:1313`.

## Content management
Adding a new piece of content to any pages can be done by adding a new post to the corresponding directories within the `content` folder. The following table shows the page and its corresponding folder

|   Page   | Home           |       People      |      Publication      |          Research         | Blog               | News               | Tool                   |
|:--------:|----------------|:-----------------:|:---------------------:|:-------------------------:|--------------------|--------------------|------------------------|
| Location | `content/home` | `content/authors` | `content/publication/publications.bib` | `content/researchproject` | `content/blogpost` | `data/news.yml` | `content/softwaretool` |

Specifically, you can follow the steps here to add to a particular page:
 - People
   - Create a new folder at `content/authors` named `{firstname}-{lastname}` where two files are placed: `_index.md` with personal information and `avatar.png` with your avatar.
   - Copy the example from `content/authors/quyu-kong/_index.md` and change the fields accordingly based on the comments.
 - Research, Blog, Tool
   - A new post to these pages is also a folder whose name will be referenced in the url path. For example, `content/newspost/test/` will be live at `https://www.behavioral-ds.science/newspost/test/`.
   - The folder should at least contains an `index.md` (note without `_`) which is consisted of two parts: the [**front matter**](https://gohugo.io/content-management/front-matter/) and the markdown content. The **front matter** defines the metadata relates to the post. Some necessary metadata fields include *title*, *authors* (should match the full name of one of the authors defined in `content/authors`), *date* and *output* (html_document). Some optional fields are: *tags*, *categories*, *links* (e.g., link to a github repo) and *header*.
   - In particular,  the **header** allows a featured image to be displayed for the post which makes it more attractive. The image can be placed in the same folder as the `index.md`.
- Publication
   - Adding a new entry to the publication page is simply done by pasting the bibtex entry to the `content/publication/publications.bib` file.
- News
   - Just adding a new entry to the `data/news.yml` file with `date` and `description`.
