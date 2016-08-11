#!/usr/bin/env ruby

# make sorted word frequency list from text

require "unicode_utils"  # allows downcasing
require "unicode"        # allows sorting

diff_re = /^(?:\+{3}|-|@@|\p{Space}(?:\p{Space}\p{Space})*(?=\P{Space}))/
word_count = Hash.new(0)
word_re = /#?(?:\p{Alnum}|-)*\p{Letter}{2,}(?:\p{Alnum}|-)*/u
ARGF.each do |line|
  next if diff_re.match line
  line.strip!
  line.scan(word_re) do |w|
    next if (w =~ /^#/)
    word_count[UnicodeUtils.downcase(w)] += 1
  end
end

word_count.keys.sort{|w,v|
  Unicode.strcmp(w,v)
}.each do |w|
  puts "%4d %s" % [word_count[w], w]
end

