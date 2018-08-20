<?php

function noStrictFunction($a,$b)
{
    return $a + $b;
}

function strictFunction(int $a, int $b):int
{
    return $a + $b;
}

echo noStrictFunction($argv[1],$argv[2]);
echo "\n";
echo strictFunction($argv[1],$argv[2]);