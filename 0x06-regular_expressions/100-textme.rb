#!/usr/bin/env ruby
begin
  res = ARGV[0].scan(/from:([^\]]+)|to:([^\]]+)|flags:([^\]]+)/)
  fin = []
  for item in res
    for str in item
      if str != nil
        fin += [str]
      end
    end
  end
  puts fin.join(',')
rescue Interrupt => e
  print_exception(e, true)
rescue SignalException => e
    print_exception(e, false)
rescue Exception => e
    print_exception(e, false)
end
