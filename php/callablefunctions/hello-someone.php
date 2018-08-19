<?php
$someone = $argv[1];

$var = function() use ($someone){
    echo "Hello " . $someone;
};

$var();