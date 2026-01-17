Write down:
What is the problem?
What input does it need?
What output should it give?
What steps are involved?

I am taking the script of my day 06.

The problem was to make a script where user will pass a file path and an output path. We will build a script where we need to accept the file path using --file and output path using --out. Also a log level filter using --level which was optional.

The input that we needed for this script to run successfully is that the user will provide the script with a file path using --file which will the log file that the user wants to analyze and the output file path using --out so that the script will write the output in the provided output file path that the user provided so that user can see the output. User can also give the level as an input in order to see the specific type of keyword inside the log file that the user is providing.

The output will be the user will be provided with the output inside the output file that the user provided the path for. The output will be the count of certain words appearing in the log file that the user provided as the input.

The steps that are involved in this script was first we will build a function that will read the log file provided by the user and we will get the count of certain words using our counter library. After that we will create another function to write the output of the count inside the output file that our user provided. Then we will use argparse library to create the arguments that the user needs to pass in order to start the script. At last we will just pass these arguments into our function. 

And our script is complete.