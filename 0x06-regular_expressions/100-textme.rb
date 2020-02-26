#!/usr/bin/env ruby
begin
  res = ARGV[0].scan(/(?<=from:|to:|flags:)[^\]]*/)
  puts res.join(',')
rescue Interrupt => e
  print_exception(e, true)
rescue SignalException => e
    print_exception(e, false)
rescue Exception => e
    print_exception(e, false)
end
