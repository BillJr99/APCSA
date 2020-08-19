---
layout: activity
permalink: /Activities/Conditionals
title: "APCSA: Intro to Computer Science - Conditionals"
excerpt: "APCSA: Intro to Computer Science - Conditionals"

info:
  next: ./Conditionals2
  
  goals: 
    - To be able to write an <code>if</code> statement
    - To design boolean expressions for conditionals
    - To implement complex conditional statements using boolean expression operators
  models:
    - model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void canRunForPresident(int age) {
                if(age >= 35) {
                    System.out.println("You are old enough to run for President of the United States!");
                }
            }
            
            public static void main(String[] args) {
                canRunForPresident(38);
            }
        }
        ]]></script>     
      title: Conditionals for Selective Execution with <code>if</code> Statements
      questions:
        - Modify the above program to return a boolean that is true if a person can run for president, and false otherwise      
      embed: |
        <iframe height="400px" width="100%" src="https://repl.it/@BillJr99/JavaFirstExample?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe> 
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-2-ifs.html
      title: The <code>if</code> Statement
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/Exercises.html
      title: <code>if</code> Statements
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit3-If-Statements/topic-3-10-practice-coding.html
      title: Code Practice with <code>if</code> Statements

tags:
  - boolean
  - expressions
  - conditionals
  
---

