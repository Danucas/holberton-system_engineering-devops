#!/usr/bin/env ruby
res = ARGV[0] #.scan(/from:([^\]]+)|to:([^\]]+)|flags:([^\]]+)/)
fin = []
for item in res
  for str in item
    if str != nil
      fin += [str]
    end
  end
end
puts fin.join(',')
