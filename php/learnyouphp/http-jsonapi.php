<?php
$path = parse_url($_SERVER['REQUEST_URI'],PHP_URL_PATH);
$iso = $_GET['iso'];
$res = [];
$time = new \DateTime($iso);
if($path === '/api/parsetime')
{
    $res = [
        "hour" =>  $time->format('H'),
        "minute" => $time->format('i'),
        "second" => $time->format('s')    
    ];
} elseif($path === '/api/unixtime'){
    $res = [
        "unixtime" => $time->format('U')
    ];
}

header('Content-Type: application/json');
echo json_encode($res);