<?php
    $filename = $argv[1];
    $file = file_get_contents($filename);
    echo substr_count($file, "\n");
     