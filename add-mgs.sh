#! /bin/bash

curl -v -X PUT -H "Content-Type: application/json" -d '{"author":"aaryab2","url":"http://172.22.152.10:24000", "name":"random"}' http://sp22-cs240-adm.cs.illinois.edu:24000/addMG;

curl -v -X PUT -H "Content-Type: application/json" -d '{"author":"atanwar2","url":"http://172.22.152.10:24004", "name":"oneblock"}' http://sp22-cs240-adm.cs.illinois.edu:24000/addMG;

curl -v -X PUT -H "Content-Type: application/json" -d '{"author":"aaryab2","url":"http://172.22.152.10:24002", "name":"target"}' http://sp22-cs240-adm.cs.illinois.edu:24000/addMG;

curl -v -X PUT -H "Content-Type: application/json" -d '{"author":"atanwar2","url":"http://172.22.152.10:24003", "name":"fish"}' http://sp22-cs240-adm.cs.illinois.edu:24000/addMG;