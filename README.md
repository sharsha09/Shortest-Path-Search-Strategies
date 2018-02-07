Input file will be of the below format

<ALGO>
<START STATE>
<GOAL STATE>
<NUMBER OF LIVE TRAFFIC LINES>
<… LIVE TRAFFIC LINES …>
<NUMBER OF SUNDAY TRAFFIC LINES>
<… SUNDAY TRAFFIC LINES …>
where:
<ALGO> is the algorithm to use and will be one of: “BFS”, “DFS”, “UCS”, “A*”.
<START STATE> is a string with the name of the start location (e.g., Home).
<GOAL STATE> is a string with the name of the goal location (e.g., StaplesCenter).
<NUMBER OF LIVE TRAFFIC LINES> is the number of lines of live traffic information that follow.
<… LIVE TRAFFIC LINES …> are lines of live traffic information , i.e., <STATE1> <STATE2> <TRAVEL TIME FROM STATE1 TO STATE2>
<NUMBER OF SUNDAY TRAFFIC LINES> is the number of lines of Sunday traffic estimates that follow.
<… SUNDAY TRAFFIC LINES …> are lines of sunday traffic information i.e., <STATE> <ESTIMATED TIME FROM STATE TO GOAL>
