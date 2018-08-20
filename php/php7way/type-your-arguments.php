<?php
function noStrictFunction($a,$b)
{
    return $a + $b;
}

function strictFunction(int $a, int $b)
{
    return $a + $b;
}

echo noStrictFunction(1,2);
echo "\n";
echo strictFunction(1,2);