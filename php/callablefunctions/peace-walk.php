<?php
array_shift($argv);
$function = function($argument){
    echo "Hello " . $argument ."\n" ;
};

array_walk($argv,$function);