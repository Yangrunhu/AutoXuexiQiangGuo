d:\learn_xi\mongodb\bin\mongod.exe --journal --config "d:\learn_xi\mongodb\mongod.cfg" --install
net start MongoDB
d:\learn_xi\mongodb\bin\mongorestore -h localhost:27017 -d learn_xi d:\learn_xi\datadump\learn_xi01
pause