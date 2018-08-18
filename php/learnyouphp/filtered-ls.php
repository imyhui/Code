<?php
    $filepath = $argv[1];
    $filetype = $argv[2];
    foreach (new DirectoryIterator($filepath) as $file)
        if($file->getExtension() == $filetype)
            echo $file."\n";