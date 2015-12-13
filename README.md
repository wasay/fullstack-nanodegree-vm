rdb-fullstack
=============

Common code for the Relational Databases and Full Stack Fundamentals courses

How to Run the Tournament application
1. Download the application (if zippd, unzip the file)
2. In command prompt /cygwin "cd" to related folder
3. Review Vagrantfile for Hyper-V box setting of hashicorp/precise64. Ajust any settings that are needed.
4. Review sync folder settings as they are setup with type "rsync"
5. Type "vagrant up" and Hit "Return Key" or "Enter Key" in command prompt.
6. If shell script is not executed, the sync folder settings will need to be adjusted.
7. Type "vagrant ssh" to ssh into the vagrant box
8. Once ssh'ed into the vagrant box.
9. Type "cd /vagrant" to go to synced folder.
10. Type "cd tournament" to go to tournament folder.
11a. Review if "tournament" database is loaded through shell script. If not:
11b. Type "psql" and enter
11c. Type "\i tournament.sql" and enter
11d. Press Ctrl + D on windows system to exit out of psql consol.
12. Type "python tournament_test.py" and enter.
13. Review that the screen prints "Success!  All tests pass!"
14. Type "vagrant halt" or "vagrant destroy" to end vagrant test.
