<?php
array_shift($argv);
function printArguments($input) {
    foreach ($input as $line) {
        yield strtoupper($line);
    }
}
$generator = printArguments($argv);
echo $generator->current()."\n";
$generator->next();
echo $generator->current()."\n";
$generator->next();
echo $generator->current();

