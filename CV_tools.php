<?php

function handle_children($json, $level)
{
    foreach ($json["sections"] as $value)
    {
        if (isset($value["name"]))
        {
            echo "<h$level>{$value["name"]}</h$level>\n";
        }
        if(!isset($value["type"]))
        {
          $value["type"]="";
        }

        if ($value["type"] == "column_break" or $value["type"] == "h_rule")
        {
            // do nothing, this is for LaTeX typesetting
        }
        elseif ($value["type"]=="text") {
          echo $value["data"];
        }
        elseif ($value["type"]=="results_vtable") {
          echo "<span class='when'>{$value["when"]}, {$value["where"]}</span>";
          echo "<table>\n\t<tr>";
          for($i=0;$i< count($value["data"]);$i++)
          {

            $j =$i % $value["cols"];
            if($j== 0){
              echo "\t</tr>\n\t<tr>\n";
            }
            $t = nl2br($value["data"][$i]);

            echo "\t\t<td>{$t}</td>\n";
          }
          echo "\t</table>\n</table>";
        }
        elseif ($value["type"]=="results_htable") {
          echo "<span class='when'>{$value["when"]}, {$value["where"]}</span>";
          echo "<table>\n";
          $k = array_keys($value["data"]);
          for($i=0;$i< count($k);$i+=$value["cols"])
          {
            echo "\t<tr>\n";
            for ($j=0; $j < $value["cols"]; $j++) {
              echo "\t\t<th>{$k[$i+$j]}</th>\n";
            }
            echo "\t</tr>\n\t<tr>\n";
            for ($j=0; $j < $value["cols"]; $j++) {
              echo "\t\t<td>{$value["data"][$k[$i+$j]]}</td>\n";
            }
            echo "\t</tr>\n";
          }
          echo "</table>";
        }
        elseif ($value["type"] == "employment")
        {
          echo "<ul>\n";
          foreach ( $value["data"] as $var2) {
            echo "\t<li>";
            if(isset($var2["name"]))
            {
              echo "<b>{$var2["name"]}</b>";
            }
            if(isset($var2["where"]))
            {
              echo ", {$var2["where"]}";
            }
            if(isset($var2["when"]))
            {
              echo " ({$var2["when"]})";
            }
            if(isset($var2["more"]))
            {
              echo "({$var2["more"]})";
            }
            echo "</li>\n";
          }
          echo "</ul>\n";
        }
        elseif ($value["type"] == "list")
        {
          echo "<ul>\n";
          foreach ( $value["data"] as $var2) {
            echo "\t<li>";
            if(isset($var2["head"]))
            {
              echo "<b>{$var2["head"]}:</b> ";
            }
            if(isset($var2["data"]))
            {
              echo $var2["data"];
            }
            if(isset($var2["url"]))
            {
              echo " <a href='{$var2["url"]}'>{$var2["url"]}</a>";
            }
            echo "</li>\n";
          }
          echo "</ul>\n";
        }
        else
        {
            echo $value["type"];
            if (isset($value["data"]))
            {
                var_dump($value["data"]);
            }
        }
        if (isset($value["sections"]))
        {
            handle_children($value, $level + 1);
        }

    }
}

function handle_CV($p)
{
    $string = file_get_contents($p);
    $json_a = json_decode($string, true);
    echo "<header>\n";
    echo "\t<span class='name'>{$json_a["name"]}</span>\n";
    echo "\t<span class='email'>{$json_a["email"]}</span>\n<br><br>\n";
    echo "\t<span class='desc'>{$json_a["desc"]}</span>\n";
    echo "</header>\n";

    handle_children($json_a, 1);
}

?>
