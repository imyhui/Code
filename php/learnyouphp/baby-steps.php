<?php
    $sum = 0;
    for($i = 1 ; $i < count($argv); $i++)
        $sum += $argv[$i];
    echo $sum;
    
    // $sum = 0;
    // unset($argv[0]);
    // foreach($argv as $num)
    //     $sum+=$num;
    // echo $sum;
