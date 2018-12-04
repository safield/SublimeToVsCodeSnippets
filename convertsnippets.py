import os
from xml.dom import minidom

#  vscode scopes
# abap
# bat
# bibtex
# clojure
# coffeescript
# c
# cpp
# csharp
# css
# diff
# dockerfile
# fsharp
# git-commit
# go
# groovy
# handlebars
# html
# ini
# java
# javascript
# javascriptreact
# json
# jsonc
# latex
# less
# lua
# makefile
# markdown
# objective-c
# objective-cpp
# perl
# php
# powershell
# jade
# python
# r
# razor
# ruby
# rust
# scss
# shaderlab
# shellscript
# sql
# swift
# typescript
# typescriptreact
# tex
# vb
# xml
# xsl
# yaml

# SUBLIME SCOPES
# source.actionscript.2
# source.applescript
# source.asp
# source.dosbatch
# source.cs
# source.c++
# source.clojure
# source.coffee
# source.css
# source.d
# source.diff
# source.erlang
# source.go
# source.dot
# source.groovy
# source.haskell
# text.html(.basic)
# text.html.jsp
# source.java
# source.java-props
# text.html.javadoc
# source.json
# source.js
# source.bibtex
# text.log.latex
# text.tex.latex.memoir
# text.tex.latex
# source.css.less
# text.tex
# source.lisp
# source.lua
# source.makefile
# text.html.markdown
# text.html.markdown.multimarkdown
# source.matlab
# source.objc
# source.objc++
# source.camlp4.ocaml
# source.ocaml
# source.ocamllex
# source.perl
# source.php
# source.regexp.python
# source.python
# source.r-console
# source.r
# source.ruby.rails
# text.haml
# source.sql.ruby
# source.regexp
# text.restructuredtext
# source.ruby
# source.sass
# source.scala
# source.shell
# source.sql
# source.stylus
# source.tcl
# text.html.tcl
# text.plain
# text.html.textile
# text.xml
# text.xml.xsl
# source.yaml

#----------------------------------------------------------------------------
# Scope class represents the matching scopes name from sublime and vscode
#----------------------------------------------------------------------------
class Scope:
    def __init__(self , sublime_name , vscode_name):
        self.sublime_name = sublime_name
        self.vscode_name = vscode_name

    def __str__(self):
        return "Sublime: "+self.sublime_name+" VSCode: "+self.vscode_name
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# SublimeSnippet
#----------------------------------------------------------------------------
class SublimeSnippet:
    def __init__(self , xmlfile):
        mydoc = minidom.parse(xmlfile)
        self.content = mydoc.getElementsByTagName('content')[0].childNodes[0].wholeText
        print "Content = "+str(content.wholeText)

#----------------------------------------------------------------------------


# main

scopeList = [
                Scope("source.c++" , "cpp"),
                Scope("source.java" , "java"),
                Scope("text.xml" , "xml")
            ]


current_dir = os.getcwd()

listOfFiles = os.listdir(current_dir)

# parse the files by valid sublime-snippet extensions
listOfSublimeSnippetFiles = list();
for file in listOfFiles:
    if file.endswith(".sublime-snippet"):
        listOfSublimeSnippetFiles.append(file)

# construct the sublime snippet classes from the files
listOfSublimeSnippets = list();
for file in listOfSublimeSnippetFiles:
    listOfSublimeSnippets.append(SublimeSnippet(file))

for file in listOfSublimeSnippetFiles:
    print(file)



# Get the list of all files in directory tree at given path
