<?php
$pdo = new PDO($argv[1]);
foreach ($pdo->query('SELECT * FROM users where age > 30') as $user) {
        echo sprintf("User: %s Age: %s Sex: %s\n",$user['name'],$user['age'],$user['gender']); 
}
$sql="UPDATE users set name= 'David Attenborough' WHERE name='".$argv[2]."'";
$pdo->exec($sql);
