<?php

$data_file=fopen("example2.txt","w");

$name=$_POST["name"];

$text_to_write=$name;

fwrite($data_file, $text_to_write);

fclose($data_file);

$out=shell_exec('python3 trailrf.py');
echo '<pre>' . $out . '</pre>';
 

?>