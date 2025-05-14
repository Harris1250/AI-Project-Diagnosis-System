===================================================================
                 Dijkstra's Algorithm with PySpark
===================================================================

Author: Muhammad Nadeem  
Course: Cloud Computing - Spring 2025  
Instructor: Dr. Lipeng Wan  

-------------------------------------------------------------------
📌 Overview
-------------------------------------------------------------------
This project implements Dijkstra’s Shortest Path algorithm using 
Apache Spark and the PySpark API. It calculates the shortest path 
distances from a single source node (node 0) to all other nodes 
in a weighted graph. The program now fully supports large, complex 
graphs and runs efficiently using Spark’s distributed computation.

-------------------------------------------------------------------
📂 Project Files
-------------------------------------------------------------------
- dijkstra.py ............ Main PySpark script  
- weighted_graph.txt ..... Input graph file (edge list format)  
- README.txt ............. This file (execution guide)  

-------------------------------------------------------------------
▶️ How to Execute
-------------------------------------------------------------------
1. Ensure that Apache Spark (v3.5.0) and Python 3 are installed and 
   available in your system’s PATH.

2. Place `dijkstra.py` and `weighted_graph.txt` in the same directory.

3. Run the following command in the terminal:

   spark-submit dijkstra.py

4. The program will output shortest path distances from node 0 
   to all other nodes. Unreachable nodes will be marked as INF.

-------------------------------------------------------------------
📥 Input File Format (weighted_graph.txt)
-------------------------------------------------------------------
- First line: number of nodes and number of edges  
- Each following line: source_node destination_node weight  

Example:

5 6  
0 1 7  
0 2 3  
1 3 9  
2 4 4  
3 4 6  
1 4 2  

The input format works for any graph size. The algorithm scales 
smoothly with larger graphs and handles heavy workloads via Spark.

-------------------------------------------------------------------
📤 Sample Output
-------------------------------------------------------------------
Shortest distances from node 0:  
Node 0: 0  
Node 1: 7  
Node 2: 3  
Node 3: 16  
Node 4: 7  

-------------------------------------------------------------------
🛠 Implementation Notes
-------------------------------------------------------------------
- Implemented using RDD transformations and joins  
- Source node is hardcoded to 0 (can be changed easily)  
- Fully tested on a complete weighted graph input  
- Successfully deployed on Ubuntu 22.04 using Microsoft Azure VM  
- Optimized for scalability and performance with large datasets  

-------------------------------------------------------------------
📧 Contact
-------------------------------------------------------------------
Muhammad Nadeem  
Email: mnadeem2@student.gsu.edu

===================================================================