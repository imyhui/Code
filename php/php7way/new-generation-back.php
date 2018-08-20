<?php
unset($argv[0]);
function printArguments($argv)
{
    foreach($argv as $r)
        yield $r;
    return array_sum($argv);
}

$func = printArguments($argv);
foreach($func as $res)
{
    echo $res ."\n";
}
echo $func->getReturn();