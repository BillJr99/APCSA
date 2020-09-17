---
layout: activity
permalink: /Activities/DataTypes
title: "APCSA: Intro to Computer Science - Overview of a Computer Program and Data Types"
excerpt: "APCSA: Intro to Computer Science - Overview of a Computer Program and Data Types"

info:
  next: ./EscapeCharacters
    
  goals: 
    - To identify the major components of a Java program, including a method and a class
    - To explain that binary data uses &quot;bits&quot; of <code>1&apos;s</code> and <code>0&apos;s</code> to represent data of various types, both numeric and textual
    - To identify primitive data structures and their uses
    - To be able to create and compile a Java source file in a chosen development environment
    - To be able to call System class methods to generate output to the console <strong>(APCSA Framework Topic 1.1 Mod 1.A)</strong>
    - To be able to identify the different primitive data types used in the Java language
    - To be able to create string literals <strong>(APCSA Framework Topic 1.1 Var 1.A)</strong>
    - To be able to identify the appropriate data type category for a particular specification. <strong>(APCSA Framework Topic 1.2 Var 1.B)</strong>
    - To be able to declare variables of the correct types to represent primitive data. <strong>(APCSA Framework Topic 1.2 Var 1.C)</strong>
  models:
    - title: "Hello World"
      model: |
        <img src="../images/examples/helloworld_annotated.png" alt="Annotated Hello World Java program example">
        <br>
        <img src="../images/examples/progelements_class.jpg" alt="Elements of a Java program: The Class">
        <br>
        <img src="../images/examples/progelements_method.jpg" alt="Elements of a Java program: The Method">
        <br>
        <table>
        <thead>
          <tr>
            <th>Character</th>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{ }</td>
            <td>Opening and closing braces</td>
            <td>Block to enclose statements</td>
          </tr>
          <tr>
            <td>( )</td>
            <td>Opening and closing parenthesis</td>
            <td>Used with methods</td>
          </tr>
          <tr>
            <td>[ ]</td>
            <td>Opening and closing brackets</td>
            <td>Used with arrays</td>
          </tr>
          <tr>
            <td>//<br>/* */</td>
            <td>Slashes</td>
            <td>Comments (single line and double line)</td>
          </tr>
          <tr>
            <td>;</td>
            <td>Semicolon</td>
            <td>End of a statement</td>
          </tr>
        </tbody>
        </table>        
      questions: 
        - What do you think the curly braces represent and enclose?
        - What character is used to end a statement of code within a method?
    - title: "Your First Program"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                // println prints a "line" to the string
                System.out.println("Hello World!");
                System.out.println("Have a great day.");
            }
        }
        ]]></script> 
      questions: 
        - What do you think the <code>//</code> characters represent?  
        - "Go to <a href=\"https://repl.it\">https://repl.it</a> and enter the code above into a file called <code>Main.java</code> (the filename is almost always the same as the class name, which we called <code>Main</code> in this example).  Click the \"Run\" button at the top to run the program."
        - "You may have noticed two commands executed before the program ran and printed \"Hello world!\" - to execute a program with the java command, the code in each class must first be compiled using the javac command.  Development environments such as repl.it usually do these steps for you.  Note that you can run many of our code examples in repl.it or the <a href=\"https://cscircles.cemc.uwaterloo.ca/java_visualize/\">Java Visualizer</a><br><img src=\"../images/examples/compileprocess.jpg\" alt=\"The compilation process\">"
        - "Change the code so that instead of printing \"Hello World!\" the code instead prints a greeting to your partner."  
        - "Change the code to the following, and execute it.<br><img src=\"../images/examples/systemoutprint.jpg\" alt=\"Printing statements to the screen\">"   
        - "What is the difference between <code>System.out.println()</code> and <code>System.out.print()</code>?  <strong>APCSA U1 Topic1.1 MOD 1.A.1 and MOD 1.A.2</strong>"
        - "What is wrong with this program?  (Debug the program).<br><img src=\"../images/examples/syntaxerror.jpg\" alt=\"A program with an error\">"
        - "Modify the program to produce the following output:<br><code>How are you?<br>Everything is going well.</code>"
    - title: Primitive Data Types
      model: |
        <a title="Hellbus / Public domain" href="https://commons.wikimedia.org/wiki/File:Odometer_rollover.jpg"><img width="512" alt="Odometer rollover" src="https://upload.wikimedia.org/wikipedia/commons/5/53/Odometer_rollover.jpg"></a>
        <br>
        <div style="width: 100%; display: table; border-collapse:separate; border-spacing:5px;">
        <div style="width: 100%; display: table-row; background-color: black; color: white;">
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Type Name</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Use</strong>
            </div>
            <div style="display: table-cell; padding:5px; width:33%; background-color: black; color: white;">
                <strong>Example</strong>
            </div>
        </div>
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>int</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Whole number numeric values
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>int participants = 40;</code>
            </div>
        </div>    
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>double</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Fractional or decimal numeric values (these are called "floating point" values)
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>double price = 5.95;</code>
            </div>
        </div>        
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                True/False
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>boolean raining = false;</code>
            </div>
        </div>  
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>char</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                A single character
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>char grade = &apos;A&apos;;</code>
            </div>
        </div>     
        <div style="width: 100%; display: table-row;">
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>String</code>
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                Textual data
            </div>
            <div style="display: table-cell; padding:5px; width:33%;">
                <code>String name = &quot;Lee&quot;;</code>
            </div>
        </div>       
        </div>
      questions:
        - What is the data type of the value <code>&quot;Hello World!&quot;</code>?
        - Observe the odometer above.  What is the place value of each of the digits in a decimal system?  How would this odometer count if the only digits it could display were 1 and 0?  What would each place value be then?
        - How might a computer represent a whole number using only 1 and 0 digits?  How do you use the decimal digits 0 through 9 to represent all whole numbers?
        - How might a computer represent a True/False boolean?
        - How might a computer represent the letter <code>&apos;A&apos;</code> or the word <code>&quot;Hi!&quot;</code>?
  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-8-practice-coding.html
      title: Mixed-Up Coding Practice
  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit1-Getting-Started/topic-1-3-variables.html
      title: "Read and watch the \"Variables\" Activity in Runestone"
tags:
  - datatypes
  
---

