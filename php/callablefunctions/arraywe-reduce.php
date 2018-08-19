<?php
array_shift($argv);
$function = function($carry, $item)
{
    $carry += $item;
    return $carry;
};
$result = array_reduce($argv, $function);
echo $result;