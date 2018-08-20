<?php
unset($argv[0]);
function upperCase($argument)
{
    (yield strtoupper($argument));
}
function printArguments ($argv)
{
    foreach($argv as $r)
    yield from upperCase($r);
}
$func = printArguments($argv);
echo $func->current()."\n";
$func->next();
echo $func->current()."\n";
$func->next();
echo $func->current();