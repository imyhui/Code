<?php
array_shift($argv);
$function = function($argument) {
    return '-' . $argument . '-';
};

$result = array_map($function, $argv);
print_r($result);