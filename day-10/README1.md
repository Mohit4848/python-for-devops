Situation
Task
Action
Result

Situation:-
Logs were growing at a very high rate. We need to 

Task:- 
I need to automate the process to know that which type of wrong thing is happening. Whether it is error, warning or any info.

Action:-
I created a python script where the user just need to give the log file using --file and an output file using --out where the user wanted to save the information of log file. I later exposed it through API using fast api.

Result:- 
The result that is obtained is that it reduced the time that was taken while reading the log file to identify the problem. With my sscript, the user just need to give the log file they want to analyze and the script will return the type of problem they are facing after analyzing the log file. The output will be given inside the output file that the user will provide with the log file as the input.