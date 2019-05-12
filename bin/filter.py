#!/usr/bin/env python

"""
Pandoc filter to convert all level 2+ headers to paragraphs with
emphasized text.
"""

from pandocfilters import toJSONFilter, toJSONFilters, Strong, Para, Header, stringify, RawInline, BlockQuote, RawBlock, Str
import json


filename = "./bin/debuglog.log" 
debugFile = open(filename, 'w')

def p(thing):
  debugFile.write(thing.encode('utf8'))
  debugFile.write("\n")

def latex(s):
    return RawBlock('latex', s)

def titleize(text):
  exceptions = ['the', 'a', 'and', 'vs']
  return ' '.join([word if word in exceptions else word.title() for word in text.split()])

################ FILTERS
################ FILTERS
################ FILTERS
################ FILTERS

def customQuote(tag, prefix, blockName):
  def replaceQuote(key, value, format, meta):
    if key == 'BlockQuote' and format == 'latex':
      if stringify(value).startswith(":" + tag):
        value[0]['c'][0] = Strong([Str(prefix)]) # remove the ":note" prefix
        return [latex("\\begin{"       + blockName +"}")] + value + [latex("\\end{"+ blockName +"}")]
  return replaceQuote

noteQuote = customQuote("note", "Note:", "noteQuote")
commentQuote = customQuote("comment", "Comment:", "commentQuote")


def titlizeHeadings(key, value, format, meta):
  if (key == 'Header'):
    size, meta, text = value
    titled = titleize(stringify(text))
    return Header(size, meta, [Str(titled)])

# def wideTables(key, value, format, meta):
#   if key == 'Table' and format == 'latex':
#     p("hellllllllllllllo")
#     p(json.dumps(value))
#     # if stringify(value[0]) == ":wide":
#     #   p("IT IS WIDE")
#     #   # return value
#     #   # p(json.dumps([latex("\\hspace{-2cm}\\begin{minipage}[c]{1.3\\linewidth}")] + [Str("HELLO")] + [latex("\\end{minipage}")]))
#     return  [latex("\\begin{"       + "minipage" +"}")] + value + [latex("\\end{"+ "minipage" +"}")]

def hmmmm(key, value, format, meta):
    p(json.dumps(key))
    if key == 'Header' and format == 'latex':
      value[1][0] = ''
      p(json.dumps(value))
    #   p("hellllllllllllllo")
    # # if stringify(value[0]) == ":wide":
    # #   p("IT IS WIDE")
    # #   # return value
    # #   # p(json.dumps([latex("\\hspace{-2cm}\\begin{minipage}[c]{1.3\\linewidth}")] + [Str("HELLO")] + [latex("\\end{minipage}")]))
    # return  [latex("\\begin{"       + "minipage" +"}")] + value + [latex("\\end{"+ "minipage" +"}")]




filters = [
  titlizeHeadings,
  noteQuote,
  commentQuote,
  hmmmm
]


if __name__ == "__main__":
  toJSONFilters(filters)
  debugFile.close()
