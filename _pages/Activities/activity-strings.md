---
layout: activity
permalink: /Activities/Strings
title: "APCSA: Intro to Computer Science - Strings"
excerpt: "APCSA: Intro to Computer Science - Strings"

info:
  next: ./StringIteration
  
  goals: 
    - To be able to explain that a <code>String</code> is a class that stores text and provides functionality that manipulates that text.
    - To be able to explain that a <code>String</code> is immutable, and that new memory is allocated for a <code>String</code> when it is modified.
    - To be able to create and manipulate a <code>String</code>.
    - To be able to invoke the <code>concat()</code>, <code>indexOf()</code>, <code>substring()</code> and <code>replace()</code> methods of a <code>String</code>.
  models:
    - title: "The <code>String</code>"
      model: |
        <script type="syntaxhighlighter" class="brush: cpp"><![CDATA[
        public class Main {
            public static void main(String[] args) {
                // These are equivalent
                // String x = "Test";
                String x = new String("Test");
                
                // So are these:
                x = "Another test";
                x = new String("Another test");
            }
        }
        ]]></script> 
      questions: 
        - Unlike re-assigning a primitive variable, assigning a variable to an object creates a new object.  A <code>String</code> is a class that allocates memory for and stores text. Since String text cannot be reassigned once it is allocated (and must be re-created instead), a <code>String</code> is called an <strong>immutable</strong> object.  Why can’t a <code>String</code> be re-assigned like an <code>int</code> or <code>double</code> can?
    - title: <code>String</code> Manipulation
      model: |
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#concat(java.lang.String)" width="100%" height="700" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#indexOf(int)" width="100%" height="600" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#indexOf(int,int)" width="100%" height="800" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replace(char,char)" width="100%" height="700" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#replace(java.lang.CharSequence,java.lang.CharSequence)" width="100%" height="480" style="pointer-events:none;" scrolling="no"></iframe>
        <br>
        <iframe src="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html#substring(int,int)" width="100%" height="640" style="pointer-events:none;"></iframe>
      questions: 
        - What is the difference between <code>x = x.concat(y)</code> and <code>x = x + y</code> for <code>String</code> objects <code>x</code> and <code>y</code>?
        - What is the difference between the two <code>indexOf()</code> methods given above? How do you know which version you are calling from a program?
        - What is the difference between the two <code>replace()</code> methods given above?  How do you know which version you are calling from a program?
      embed: |
        <iframe height="400px" width="100%" src="https://BillJr99.github.io/APCSA/assets/code-viewer.html?zip=https%3A%2F%2Fraw.githubusercontent.com%2FBillJr99%2FAPCSA%2Fgh-pages%2Fassets%2Freplit%2FJavaFirstExample.zip&title=Java%20First%20Example" scrolling="yes" frameborder="no" allowfullscreen="true" sandbox="allow-scripts allow-same-origin"></iframe>

  additional_reading:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-6-strings.htm	
      title: Strings
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-7-string-methods.html
      title: String Methods

  additional_practice:
    - link: https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-12-practice-coding.html
      title: Coding with Objects
    
  try_partner:
    - "<code>String</code> Manipulation: <a href=\"https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html\">https://runestone.academy/runestone/books/published/csawesome/Unit4-Iteration/FRQstringScrambleA.html</a>"

  try_own:
    - "Write a function that accepts two <code>String</code> parameters (<code>a</code> and <code>b</code>), and returns <code>true</code> if they contain the same text, or <code>false</code> otherwise."
    
tags:
  - strings
  
---

