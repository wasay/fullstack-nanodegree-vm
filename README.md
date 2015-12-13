rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

How to Run the Tournament application

0. Download the application (if zippd, unzip the file)
0. In command prompt /cygwin "cd" to related folder
0. Review Vagrantfile for Hyper-V box setting of hashicorp/precise64. Ajust any settings that are needed.
0. Review sync folder settings as they are setup with type "rsync"
0. Type "vagrant up" and Hit "Return Key" or "Enter Key" in command prompt.
0. If shell script is not executed, the sync folder settings will need to be adjusted.
0. Type "vagrant ssh" to ssh into the vagrant box
0. Once ssh'ed into the vagrant box.
0. Type "cd /vagrant" to go to synced folder.
0. Type "cd tournament" to go to tournament folder.
0. a. Review if "tournament" database is loaded through shell script. If not:
0. b. Type "psql" and enter
0. c. Type "\i tournament.sql" and enter
0. d. Press Ctrl + D on windows system to exit out of psql consol.
0. Type "python tournament_test.py" and enter.
0. Review that the screen prints "Success!  All tests pass!"
0. Type "vagrant halt" or "vagrant destroy" to end vagrant test.
