#!/usr/bin/env ruby
#puts ARGV[0].scan(/from:\+?\d{11}?[a-zA-Z]?,to:\+?\d{11}[a-zA-Z]?,flags:\d{1}:\d{1}:\d{1}:\d{1}/).join()
puts ARGV[0].scan(/^\d{11}?$/).join()
