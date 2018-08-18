<?php
$filepath = $argv[1];
$filetype = $argv[2];
require_once __DIR__. '/DirectoryFilter.php';
$myFilter = new DirectoryFilter;
echo $myFilter->filter($filepath,$filetype);