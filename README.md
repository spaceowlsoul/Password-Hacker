# :sunglasses: Password-Hacker

All sorts of creatures lurk around the Internet, including trolls, pirates, miners – and hackers 😜
This project is dedicated to trying to connect to a secret server, hack the password in the quickest way possible without being caught!

## How to hack? :smirk:

1.To start download the 'main.py' file and copy the path to it.

2.Run the command prompt, paste the copied path and start executing the python file as follows:
    
      python main.py {IP address} {port}

  For example:
  
      python hack.py localhost 9090
 
 3.Using the list of frequently used admin logins from the [file](https://github.com/spaceowlsoul/Password-Hacker/blob/main/logins.txt), the program will try every possible password from the list of uppercase and lowercase letters and digits until it gets the correct one. 
   In order not to be revealed, this hacking program uses the delay in the server response when password starts with the correct symbols made by the admin's patch.
   
 4.As a result, you'll see the JSON-string with the pair of the correct login and password. Like this:
 
      python hack.py localhost 9090
      {"login": "admin3", "password": "mlqDz33x"}
      
That's it! You're brilliant!
