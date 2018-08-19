<?php
array_shift($argv);
$function = function($number) {
    return $number %2 == 0;
};

$res = array_filter($argv, $function);
asort($res);
print_r($res);