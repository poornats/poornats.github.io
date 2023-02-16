<?php
 header('Access-Control-Allow-Origin: *');
 $RID = $_POST['RID'];
 $opened = 0;
 $filename = 'logData/logData_all.csv';

 if (($handle = fopen($filename, "r")) !== FALSE) {
  while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
      
      
      if ($data[0] == $RID){
          $opened = 1;
      }
      
  }
  
  fclose($handle);
}

if ($opened == 0){
  $f = fopen($filename, 'a');
    
  fwrite($f, $RID );
  
  fclose($f);

}

echo  json_encode($opened);
?>