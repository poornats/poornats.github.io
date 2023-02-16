<?php
    $data = $_POST['logJson'];
    
    $obj = json_decode($data);
    $pid = $obj->{'participantID'};
    
    $filename = 'logData/logData'.'_'.strval($pid).'.json';
    
    $data = $data. ',
    ';
    
    $f = fopen($filename, 'a');
    
    fwrite($f, $data );
    
    fclose($f);
    
?>