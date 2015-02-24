#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: sort_test.pl
#
#        USAGE: ./sort_test.pl  
#
#  DESCRIPTION: Test Sorting
#               
#
#        NOTES: inspired by http://www.perl.com/pub/2012/06/perlunicook-make-cmp-work-on-text-instead-of-codepoints.html
#      VERSION: 1.0
#      CREATED: 2012-06-09
#  Last Change: 2015-02-24, 15:35:27 CET
#===============================================================================

use strict;
use warnings;
use utf8;
# binmode(STDIN,":utf8");
# binmode(STDERR,":utf8");
# binmode(STDOUT,":utf8");
use open qw( :encoding(UTF-8) :std );

# only if DATA is used:
binmode(DATA, ":encoding(UTF-8)");

# use charnames qw( :full :short );
use feature qw(say state switch unicode_strings);
use autodie;
use open qw( :encoding(UTF-8) :std );
use IO::Handle;
use v5.14;

use Unicode::Collate;

my $es = Unicode::Collate->new(
    # level         => 1,
    level         => 2,
    ignore_level2 => 1, # By default, case-sensitive comparison (that is level 3 difference) won't ignore accents (that is level 2 difference).
    normalization => undef,
    # normalization => "NFKD",
);

chomp(my @words = <DATA>);

@words = map  { $_->[0] }
    sort { $a->[1] cmp $b->[1] }
    map  { [$_, $es->getSortKey($_)] }
        @words;

say join("\n", @words);

# DATA also contains words in NFD (o+umlaut instead of ö)
__END__
ärger
Ärger
Ärg
ärg
arg
Arg
Brötchen
Würstchen
Wurstchen
Wurst
Stanisław
Stanislaw
Stanisłaus
Stanislaus
Pena
Peña
Peña
Pena
Schröder
Schröder
Schroder
