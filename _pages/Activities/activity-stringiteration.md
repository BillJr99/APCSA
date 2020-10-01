---
layout: activity
permalink: /Activities/StringIteration
title: "APCSA: Intro to Computer Science - Iteration with Strings"
excerpt: "APCSA: Intro to Computer Science - Iteration with Strings"

info:  
  prev: ./Strings
  
  goals: 
    - To be able to apply iteration and conditionals to a <code>String</code>

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-3-strings-loops.html 
      title: <code>String</code> Loops 
     
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html
      title: <code>String</code> Iteration    
    - link: https://repl.it/community/classrooms/20700/assignments/146533
      title: Looping over Every Other Character of a <code>String</code>
    - link: https://repl.it/community/classrooms/20700/assignments/146572
      title: Printing Only the Vowels of a <code>String</code>

  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[        
        public class Main {
            public static void main(String[] args) {
                String x = "test";
                
                boolean containsT = false;
                int numT = 0;
                
                for(int i = 0; i < x.length(); i++) {
                    if(x.charAt(i) == 't') {
                        containsT = true;
                        numT++;
                    }
                }
            }
        }
        ]]></script>     
      title: Iterative Algorithms Using the <code>String</code>
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
      questions:
        - "For what values of <code>i</code> will the character <code>&lsquo;t&rsquo;</code> be found in this <code>String</code>?  You may find the <a href=https://cscircles.cemc.uwaterloo.ca/java_visualize/>Java Visualizer</a> or your IDE debugger helpful."
        - "Write a function that accepts a <code>String x</code>, a <code>char c</code>, and an <code>int n</code>.  Return the index of the <code>n&rsquo;th</code> instance of the character <code>c</code> in the <code>String x</code>.  Use the <code>indexOf()</code> method in a loop."
  try_partner:
    - "Iteration: <a href=\"https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-8-practice-coding.html\">https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/topic-4-8-practice-coding.html</a>"
    - "Write a function that accepts a String <code>x</code>, a <code>char</code> <code>c</code>, and an <code>int</code> <code>n</code>.  Return the index of the <code>n</code>’th instance of the character <code>c</code> in the <code>String</code> <code>x</code>.  Use the <code>indexOf()</code> method in a loop."
    - "Write a function that accepts a String, and determines if that <code>String</code> is a palendrome."    

  try_own:
    - "Self Divisors using the Modulus, Loops, and Conditionals: <a href=\"https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQselfDivisorA.html\">https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQselfDivisorA.html</a>"
  
tags:
  - iterations
  - strings
  
---

