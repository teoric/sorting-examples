# Scripts to generate sorted word lists

I always forget how to sort (German) word lists sensibly with Python,
Ruby, Perl or on the Shell on the Mac.


# Ruby does not seem to sort on anything else than character number by default. [http://rubygems.org/gems/unicode](Unicode) and [http://unicode-utils.rubyforge.org](Unicode Utils) help.

- Python and Perl do, but rely on locale, which seems to be broken on the Mac. For Perl, [Unicode::Collate](http://search.cpan.org/~sadahiro/Unicode-Collate/Collate.pm)(::Locale) is part of the core modules. For
Python, there is [pyuca](https://github.com/jtauber/pyuca).

- `sort` (both BSD and GNU) seems to be similary broken. `ucsort` from [Unicode::Tussle](http://search.cpan.org/~bdfoy/Unicode-Tussle/) can replace them.


