# aspatrix_file_parsing_and_reasoning_with_args
(Formal Argumentation) This project is to create an end-to-end system that can parse files and reason with arguments.<br>
<br>
The “conflict_free” function takes as an input the data parsed from **aspartix_parser.py** read_file function, as two sets arguments and attacks. The function creates the set of all possible arguments from input ‘arguments’ set. Then it iterates the attacks set inside of the loop of different combinations. The aim is to find the combinations which will not contain any attacks between elements in the set. When the correct set found the function checking if this set is the subset of the set included into the list to derive only maximum sets. The combination sets are pre-sorted from biggest to smallest, which gives the possibility to include biggest sets first.<br>
<br>
The Python program **semantics.py** returns the maximal (for set inclusion) conflict-free, admissible, and preferred semantics for a given argumentation graph represented as a file in the ASPARTIX format.
