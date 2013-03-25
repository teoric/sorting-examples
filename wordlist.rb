#!/usr/bin/env ruby

require "unicode_utils"  # allows downcasing
require "unicode"        # allows sorting

diff_re = /^(?:\+{3}|-{3})/
word_count = Hash.new(0)
splitter_re = /[^[:word:]-]+/
diff_indy_re = /^[\+-]/
ARGF.each do |line|
  next if diff_re.match line
  line.split(splitter_re).each do |w|
    line.sub(diff_indy_re, "")
    word_count[UnicodeUtils.downcase(w)] += 1
  end
end

word_count.keys.sort{|w,v|
  Unicode.strcmp(w,v)
}.each do |w|
  puts "%4d %s" % [word_count[w], w]
end

