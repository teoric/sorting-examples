#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: wordlist.pl
#
#        USAGE: ./wordlist.pl  
#
#  DESCRIPTION: make word frequency list from text
#
#      CREATED: 24.03.2013 22:47:23
#  Last Change: 2013-03-27, 21:41:48 CET
#===============================================================================

# BOILERPLATE:
use strict;
use warnings;
use utf8;
# binmode(STDIN,":utf8");
# binmode(STDERR,":utf8");
# binmode(STDOUT,":utf8");
use open qw( :encoding(UTF-8) :std );
# use charnames qw( :full :short );
# use feature qw(say state switch unicode_strings);
use feature qw(unicode_strings);
use re "/u";
use autodie;
use v5.14;



# SORTING SET UP:
#
# without locale:
# use Unicode::Collate;
# my $Collator = Unicode::Collate->new(); # unbreak sorting on Mac
# alternatively, with Locale:
use Unicode::Collate::Locale;
my $Collator = Unicode::Collate::Locale->new(locale => "de_DE"); # unbreak sorting on Mac
my $sort = $Collator->sort;

# COUNT
my %words;
while (<>){
    next if (m/^(?:@@|\+{3}|\-|\s(?:\s\s)*(?=\S))/);
    while (m/#?(?:\w|-)*\p{L}{2,}(?:\w|-)*/g){
        next if ($& =~ /^#/); # skip IDs
        $words{lc($&)}++;
    }
}

# SORT & PRINT (1)
for my $word ($Collator->sort(keys(%words))){
    printf("%4d %s\n", $words{$word}, $word);
}

# SORT & PRINT (2)
# # for non-Macs with working locale:
# use locale;
# for my $word (sort(keys(%words))){
#     printf("%4d %s\n", $words{$word}, $word);
# }
