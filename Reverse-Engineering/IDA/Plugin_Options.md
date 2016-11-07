
## Plugin Options

The -O command line switch allows the user to pass options to the plugins. A plugin which uses options should call the get_plugin_options() function to get them.

  Since there may be plugins written by independent programmers, each options will have a prefix -O in front of the plugin name.

  For example, a plugin named "decomp" should expect its parameters to be in the following format:

      -Odecomp:option1:option2:option3

In this case, get_plugin_options("decomp") will return the "option1:option2:option3"  part of the options string.

  If there are serval -O options in the command line, they will be concatenated with ':' between them.
