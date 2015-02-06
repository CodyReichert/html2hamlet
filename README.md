html2hamlet
===========

A simple python script that takes an html file and outputs a hamlet file for use with Yesod

### Installation

The only dependency is Beautiful Soup (used for parsing the HTML). You can optionally use a
virtual environment or install the dependecies globally:

    $ git clone git@github.com:CodyReichert/html2hamlet
    $ cd html2hamlet/

(optional)

    $ virtualenv venv
    $ source venv/bin/activate

(required)

    $ pip install beautifulsoup4
    $ python html2hamlet.py YOUR_HTML_FILE

#### Usage

Run:
    
    python html2hamlet.py "filename.html"
    
This will output filename.hamlet into the current directory

#### Features
Run this script with any html file as the first argument. The output will be a
`.hamlet` file in the current directory. All end tags are removed, all classes in any element are
transformed to proper hamlet syntax. For example:

    <div class="foo">
    </div>

becomes

    <div .foo> 

And the same for Id's:

    <div class="foo" id="bar">
    </div>

becomes

    <div .foo #bar>

Img `src` attributes are also transformed. If you move all of the static images to the `/static/img/`
directory of your yesod project, this *should* take care of the rest. For example:

    <img class="thumbnail" src="/static/img/myimg.jpg">

becomes:

    <img .thumbnail src=@{StaticR_img_myimg_jpg}>

*Note: img src links that start with `http` are omitted, so any images you're linking to will be ok*

#### TODO

- Preserver HTML comments
  - Currently it's stripping all comments because comments that end on the same
    line as a closing tag (e.g. <code></ close> --></code>) get removed and the comment would never end.
- Two space indent in target file instead of 1 space.
- Keep BS from putting html and body tags at the top of every file.
- Transforming links (things to keep in mind):
  - href's that start with a hash (#) probably don't need to be transformed to @{LinkR}
