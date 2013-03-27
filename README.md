# Sorting (Perl, Python, Ruby, Shell) on the Mac

*illustrated with simple scripts to generate sorted word lists*

I always forget how to sort word lists that also contain non-ASCII characters (basically any letters except `[A-Za-z]`, e.g. accented characters, non-Latin script, etc.) sensibly with Python,
Ruby, Perl or on the Shell on the Mac. The specific problem is that the Mac locale support seems to be broken w.r.t. sorting.

The packages below help to sort strings according to the [Unicode collation algorithm](http://www.unicode.org/reports/tr10/). They are platform-independent and also work on the Mac.

- [Ruby](ruby-lang.org) does not seem to sort on anything else than character number by default. [http://rubygems.org/gems/unicode](Unicode) and [http://unicode-utils.rubyforge.org](Unicode Utils) help:
    - `UnicodeUtils.downcase`, `UnicodeUtils.upcase` etc.
    - `Unicode.strcmp`

- [Python](http://www.python.org) and [Perl](http://www.perl.org) can sort non-ASCII strings, but they rely on the locale setting (which seems to be broken on the Mac). For Perl, [Unicode::Collate](http://search.cpan.org/~sadahiro/Unicode-Collate/Collate.pm)(::Locale) is part of the core modules. For
Python, there is [pyuca](https://github.com/jtauber/pyuca).

- `sort` (both BSD and GNU) also does not work for me. `ucsort` from [Unicode::Tussle](http://search.cpan.org/~bdfoy/Unicode-Tussle/) can replace them. Unicode::Tussle has heavy dependencies; but  [ucsort (direct Link to code)](http://cpansearch.perl.org/src/BDFOY/Unicode-Tussle-1.03/script/ucsort) does not.


# Example Scripts

The example scripts prepare word frequency lists for Markdown documents and patches to these. For patches, the [unified format](http://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html) is assumed and for [Markdown](http://daringfireball.net/projects/markdown/) documents, an even number of spaces for indentation, so that lines that start with an uneven number of spaces are definitely patch context lines and can be skipped. See [grundgesetz-dev](https://github.com/bheisig/grundgesetz-dev) for a playground to use these.
