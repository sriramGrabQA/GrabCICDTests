<!DOCTYPE html>
<html>
      
<head>
    <title>
        How to call PHP function
        on the click of a Button ?
    </title>
</head>
  
<body style="text-align:center;">
      
    <h1 style="color:green;">
        Run API and DB Tests
    </h1>
      
    <h4>
        click below
    </h4>
      
    <?php
        if(array_key_exists('button', $_POST)) {
            button();
        }
        // execInBackground('start cmd.exe @cmd /k "python -m robot E2E.robot"');

        function button() {
            execInBackground('start cmd.exe @cmd /k "cd C:\Users\THIS PC\PycharmProjects\GrabRobot && python -m robot E2E.robot"');
        }

        function execInBackground($cmd) { 
            if (substr(php_uname(), 0, 7) == "Windows"){ 
                pclose(popen("start /B ". $cmd, "r"));  
            } 
            else { 
                exec($cmd . " > /dev/null &");   
            } 
        }
    ?>
  
    <form method="post">
        <input type="submit" name="button"
                class="button" value="Button" />

    </form>
</head>
  
</html>