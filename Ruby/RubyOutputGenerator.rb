require_relative 'RubyModuleChecker'
params = nil
ARGV.each do|a|
  params = a
end
output = Testing.setup(params)
print(output)