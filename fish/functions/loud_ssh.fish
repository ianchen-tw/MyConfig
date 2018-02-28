function loud_command 
  echo $argv[1]; and eval $argv[2]
end
function loud_ssh
  set --local user      $argv[1]
  set --local host      $argv[2]
  set --local host_alias $argv[3]
  if test "$host_alias" = ""
    loud_command "Login to $user@$host" "ssh $user@$host"
  else 
    loud_command "Login to $user@$host_alias" "ssh $user@$host"
  end
end
